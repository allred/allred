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

def print_stores():
    logging.debug("logging test")
    simco = Simco()
    #simco.silog('silog loggarooba')
    dict_ticker, datetime_simco_latest = get_dict_ticker_from_log()
    print(f"{datetime_simco_latest} [profit per hour, exchange -> retail]")
    try:
        rc = redis_client()
    except Exception as e:
        print(f"FAILURE: {e}")
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
                    print(f"[DEBUG: {k['name']}:{k['kind']} usph={round(units_sold_per_hour,2)} arp={round(average_retail_price,2)} sat={round(market_saturation,2)}]")
                    revenue_per_hour = units_sold_per_hour * k['revenue_less_wages_per_unit']
                else:
                    print(f"no redis data for {k['name']}")
        profit_per_hour[k['name']] = round(revenue_per_hour - exchange_cost_to_fill_one_hour, 2)
        d_sorted = dict(sorted(profit_per_hour.items(), key=lambda x: x[1], reverse=True))
        print(f"  [{s['name'].upper()}] {d_sorted}")
    if len(kinds_not_found) > 0:
        logging.warning(f"WARNING: {len(kinds_not_found)} not in ticker")

def print_stores_web():
    html_start = """
<!DOCTYPE html>
<html>
  <head>
        <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
  </head>
  <body>
    <pre><code>
"""
    print(html_start)
    print_stores()
    print("""
    </code></pre>
  </body>
</html>
""")

if __name__ == '__main__':
    args = docopt(usage, version='665')
    #print(args)
    if args.get("-w"):
        print_stores_web()
    else:
        print_stores()
