#!/usr/bin/env python
usage = f"""
Usage:
    {__file__} [-h] [-d] [-r] [-w]

Options:
    -h --help      Show this screen.
    -d             Debug mode.
    -r             Redis mode. Source resources from redis.
    -w             Web output
"""
import json
import math
import os
import sys
import time
from datetime import datetime
from docopt import docopt
from simco_base import *
from util_status_resources import get_resource_statuses

"""
const timeModeling = (retailModeling, saturation, amount, price) => eval(retailModeling);

const timeToSellUnits = (quantity, salesModifier, price, quality, marketSaturation, retailModeling) => {
  const qAllowance = 2;

  const adjusted_market_saturation = Math.max(marketSaturation - quality*0.24, 0.1 - 0.24*qAllowance);

  const tts = timeModeling(retailModeling, adjusted_market_saturation, quantity, price);

  return Math.ceil(tts - tts*salesModifier/100.0);

};

const unitsSoldAnHour = (salesModifier, price, quality, marketSaturation, retailModeling) => {

  const secondsToProduce100units = timeToSellUnits(100, salesModifier, price, quality, marketSaturation, retailModeling);

  return 100*3600/secondsToProduce100units;

};


"""

# salesModifier comes from authUser (me.json ie, 3 for me, ie +3%)
def time_to_sell_units(quantity, salesModifier, price, quality, marketSaturation, retailModeling):
    qAllowance = 2
    adjusted_market_saturation = max(marketSaturation - quality*0.24, 0.1 - 0.24*qAllowance)
    tts = retailModeling
    rvalue = math.ceil(tts - tts*salesModifier/100)
    return rvalue

def units_sold_an_hour(salesModifier, price, quality, marketSaturation, retailModeling):
    secondsToProduce100units = time_to_sell_units(100, salesModifier, price, quality, marketSaturation, retailModeling)
    return 100*3600/secondsToProduce100units

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
        profit_per_hour = defaultdict(dict)
        profit_per_hour_redis = {}
        kinds_not_found = []
        for k in s['kinds']:
            revenue_per_hour = k.get("units_sold_per_hour") * k.get("revenue_less_wages_per_unit")
            kind = k.get("kind")
            if not kind in dict_ticker:
                kinds_not_found.append(kind)
                continue
            market_price_per_unit = dict_ticker.get(k.get('kind'), 1000000) # default is a dummy value to throw the result way off
            exchange_cost_to_fill_one_hour = k.get("units_sold_per_hour") * market_price_per_unit
            pph = round(revenue_per_hour - exchange_cost_to_fill_one_hour, 2)
            if not args.get("-r"):
                profit_per_hour[k['name']]["f"] = pph
            if not args.get("-r") or not rc:
                continue
            json_res = rc.hget("simco:resources", f"{k['kind']}:json")
            if not json_res:
                logging.debug(f"no redis data for {k['name']}")
                continue
            try:
                json_res = json.loads(json_res)
            except Exception as e:
                logging.error(e)
                continue
            # REDIS MODE
            retail_modeling = json_res.get("retailModeling")
            if not retail_modeling:
                if args.get("-d"):
                    logging.debug(f"kind {k} has no retailModeling, may be aerospace item")
                continue
            average_retail_price = json_res.get("averageRetailPrice")
            market_saturation = json_res.get("marketSaturation")
            hash_formula = retail_modeling_parse(retail_modeling)
            quantity = 100
            time_modeling = retail_modeling_calculate(hash_formula, average_retail_price, market_saturation, quantity)
            sales_modifier_me = 3
            quality = 0
            redis_units_sold_per_hour = units_sold_an_hour(sales_modifier_me, average_retail_price, quality, market_saturation, time_modeling)
            revenue_per_hour_redis = redis_units_sold_per_hour * k.get("revenue_less_wages_per_unit")
            if args.get("-d"):
                logging.debug(f"[DEBUG: {k['name']}:{k['kind']} rusph={round(redis_units_sold_per_hour,2)} tmodeling={round(time_modeling,2)} arp={round(average_retail_price,2)} sat={round(market_saturation,2)}]")
            exchange_cost_to_fill_one_hour_redis = redis_units_sold_per_hour * market_price_per_unit
            pph_redis = round(revenue_per_hour_redis - exchange_cost_to_fill_one_hour_redis, 2)
            percent_diff = round(100*(pph/pph_redis), 2)
            profit_per_hour[k.get("name")]["r"] = pph_redis 
        sort_key = "f"
        if args.get("-r"):
            sort_key = "r"
            items2 = {k:v[sort_key] for k,v in sorted(profit_per_hour.items())}
            items2 = dict(sorted(items2.items(), key=lambda x: x[1], reverse=True))
            d_sorted = items2
        else:
            d_sorted = dict(sorted(profit_per_hour.items(), key=lambda x: x[1][sort_key], reverse=True))
        out_report.append(f"  [{s['name'].upper()}] {d_sorted}")
    if len(kinds_not_found) > 0:
        logging.warning(f"WARNING: {len(kinds_not_found)} not in ticker")

    try:
        resource_statuses = get_resource_statuses()
        newest_resource = ""
        oldest_resource = ""
        for k, v in sorted(resource_statuses.items(), key=lambda y: str(y[1]), reverse=True):
            tstamp_resource = datetime.fromtimestamp(v)
            tstamp_now = datetime.now()
            tdiff = tstamp_now - tstamp_resource
            seconds_in_day = 24 * 60 * 60
            if not newest_resource:
                newest_resource = f"{k} {str(tstamp_resource)} {tdiff.seconds}"
                newest_daysec = divmod(tdiff.days * seconds_in_day + tdiff.seconds, 60)
            oldest_resource = f"{k} {str(tstamp_resource)} {tdiff.seconds}"
            oldest_daysec = divmod(tdiff.days * seconds_in_day + tdiff.seconds, 60)
        out_report.append(f"[newest] {newest_resource} min,sec={newest_daysec}")
        out_report.append(f"[oldest] {oldest_resource} min,sec={oldest_daysec}")
    except Exception as e:
        logging.warning(f"{e}")
    return out_report, dict_header

def print_stores():
    list_out, dict_header = gen_stores()
    for line in list_out:
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
    <div class="container black blue-text text-darken-2">
""")

    header_printed = False
    re_store = re.compile('^.*(?P<label>\[\S+\])(?P<wares>.*)')
    for line in list_stores:
        if header_printed:
            m = re_store.search(line)
            if not m:
                continue
            groupdict = m.groupdict()
            print(f'''
<div class="row">
  <div class="col s2"><h6>{groupdict["label"]}</h6></div>
  <div class="col s10"><h3>{groupdict["wares"]}</h3></div>
</div>''')
        else:
            print(f'<div class="row"><div class="col s12">{line}</div></div>')
            print(f'<div class="divider"></div>')
            header_printed = True

    print(f"""
    <!--h2>{dict_header['t']}</h2-->
    <h2><script>document.write("report generated " + Math.floor(Math.floor(Date.now()/1000 - {time.time()}) / 60) + "m ago")</script></h2>

    <!--
    <h2><a href="https://snapshot.raintank.io/dashboard/snapshot/bkvCQJyglvsj6scy3jz6x3BV867kFZn6">snapshot</a></h2>

    <iframe src="https://piloto.grafana.net/d-solo/6M9c_9EGz/rp2-system-blah?orgId=1&from=1613613580262&to=1613635180262&panelId=2" width="450" height="200" frameborder="0"></iframe>

    <h2>img</h2>
    <img src="https://piloto.grafana.net/render/d-solo/6M9c_9EGz/rp2-system-blah?orgId=1&from=1613631456634&to=1613635056634&panelId=2&width=1000&height=500&tz=America%2FNew_York">
    -->

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
