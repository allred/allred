#!/usr/bin/env python
import json
import os
import sys
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

if __name__ == '__main__':
    print_stores()
