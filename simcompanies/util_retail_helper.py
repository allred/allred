#!/usr/bin/env python
usage = f"""
Usage: 
    {__file__} [-h] [-w]

Options:
    -h --help      Show this screen.
    -w             Web output
"""
import json
import os
import sys
from docopt import docopt
from simco_base import *

def gen_stores():
    out_report = []
    simco = Simco()
    #simco.silog('silog loggarooba')
    dict_ticker, datetime_simco_latest = get_dict_ticker_from_log()
    dict_header = {
        "t": datetime_simco_latest,
        "blurb": "[profit per hour, exchange -> retail]",
    }
    out_report.append(list(v for k,v in dict_header.items()))
    try:
        rc = redis_client()
    except Exception as e:
        logging.error(f"FAILURE: {e}")
    for s in stores:
        profit_per_hour = {}
        kinds_not_found = []
        for k in s['kinds']:
            revenue_per_hour = k['units_sold_per_hour'] * k['revenue_less_wages_per_unit']
            kind = k.get("kind")
            if not kind in dict_ticker:
                kinds_not_found.append(kind)
                pass
            market_price_per_unit = dict_ticker.get(k.get('kind'), 1000000)
            exchange_cost_to_fill_one_hour = k['units_sold_per_hour'] * market_price_per_unit
            profit_per_hour[k['name']] = round(revenue_per_hour - exchange_cost_to_fill_one_hour, 2)
            if False and rc:
                json_res = rc.hget("simco:resources", f"{k['kind']}:json")
                if json_res:
                    json_res = json.loads(json_res)
                    retail_modeling = json_res["retailModeling"]
                    average_retail_price = json_res["averageRetailPrice"]
                    market_saturation = json_res["marketSaturation"]
                    hash_formula = retail_modeling_parse(retail_modeling)
                    units_sold_per_hour = retail_modeling_calculate(hash_formula, average_retail_price, market_saturation, 100)
                    logging.debug(f"[DEBUG: {k['name']}:{k['kind']} usph={round(units_sold_per_hour,2)} arp={round(average_retail_price,2)} sat={round(market_saturation,2)}]")
                    revenue_per_hour = units_sold_per_hour * k['revenue_less_wages_per_unit']
                else:
                    logging.debug(f"no redis data for {k['name']}")
        profit_per_hour[k['name']] = round(revenue_per_hour - exchange_cost_to_fill_one_hour, 2)
        d_sorted = dict(sorted(profit_per_hour.items(), key=lambda x: x[1], reverse=True))
        out_report.append(f"  [{s['name'].upper()}] {d_sorted}")
    if len(kinds_not_found) > 0:
        logging.warning(f"WARNING: {len(kinds_not_found)} not in ticker")
    return out_report, dict_header

def print_stores():
    out, dict_header = gen_stores()
    for line in out:
        print(line)

def print_stores_web():
    list_stores, dict_header = gen_stores()
    print("""
<!DOCTYPE html>
<html>
  <head>
        <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
  </head>
  <body>
    <div class="container">
""")

    header_printed = False
    re_store = re.compile('^.*(?P<label>\[\S+\])(?P<wares>.*)')
    for line in list_stores:
        if header_printed:
            m = re_store.search(line)
            groupdict = m.groupdict()
            print(f'''
<div class="row">
  <div class="col s2">{groupdict["label"]}</div>
  <div class="col s10">{groupdict["wares"]}</div>
</div>''')
        else:
            print(f'<div class="row"><div class="col s12">{line}</div></div>')
            print(f'<div class="divider"></div>')
            header_printed = True

    print(f"""
    <h1>{dict_header['t']}</h1>
    </div>
  </body>
</html>
""")

if __name__ == '__main__':
    args = docopt(usage, version='665')
    if args.get("-w"):
        print_stores_web()
    else:
        print_stores()
