#!/usr/bin/env python
import json
import os
import redis
from datetime import datetime

token_redis = os.environ["SIMCO_REDIS_TOKEN"]
uri_redis = f"redis://{token_redis}@redis-10827.c8.us-east-1-4.ec2.cloud.redislabs.com:10827"
redis_list_ticker = "simco:ticker_json"

# get these values from the Encyclopedia
stores = [
    {
        "name": "car_dealership",
        "kinds": [
            {
                "name": "economy_car",
                "kind": 55,
                "units_sold_per_hour": 1.65,
                "revenue_less_wages_per_unit": 2274.30,
            },
            {
                "name": "economy_e_car",
                "kind": 53,
                "units_sold_per_hour": 1.45,
                "revenue_less_wages_per_unit": 3393.24,
            },
            {
                "name": "truck",
                "kind": 57,
                "units_sold_per_hour": 0.64,
                "revenue_less_wages_per_unit": 5697.5,
            },
        ],
    },
    {
        "name": "electronics",
        "kinds": [
            {
                "name": "smart_phones",
                "kind": 24,
                "units_sold_per_hour": 1.85,
                "revenue_less_wages_per_unit": 648.86,
            },
            {
                "name": "tvs",
                "kind": 28,
                "units_sold_per_hour": 1.38,
                "revenue_less_wages_per_unit": 954.10,
            },
        ],
    },
    {
        "name": "fashion",
        "kinds": [
            {
                "name": "underwear",
                "kind": 60,
                "units_sold_per_hour": 23.80,
                "revenue_less_wages_per_unit": 8.14,
            },
            {
                "name": "gloves",
                "kind": 61,
                "units_sold_per_hour": 16.74,
                "revenue_less_wages_per_unit": 16.06,
            },
            {
                "name": "sneakers",
                "kind": 65,
                "units_sold_per_hour": 25.65,
                "revenue_less_wages_per_unit": 16.87,
            },
        ],
    },
    {
        "name": "hardware",
        "kinds": [
            {
                "name": "bricks",
                "kind": 102,
                "units_sold_per_hour": 78.47,
                "revenue_less_wages_per_unit": 3.49,
            },
            {
                "name": "cement",
                "kind": 103,
                "units_sold_per_hour": 54.16,
                "revenue_less_wages_per_unit": 7.36,
            },
            {
                "name": "planks",
                "kind": 108,
                "units_sold_per_hour": 96.36,
                "revenue_less_wages_per_unit": 10.05,
            },
        ],
    },
    {
        "name": "grocery",
        "kinds": [
            {
                "name": "apples",
                "kind": 3,
                "units_sold_per_hour": 83.64,
                "revenue_less_wages_per_unit": 2.16,
            },
            {
                "name": "oranges",
                "kind": 4,
                "units_sold_per_hour": 64.82,
                "revenue_less_wages_per_unit": 2.25,
            },
            {
                "name": "eggs",
                "kind": 9,
                "units_sold_per_hour": 278.42,
                "revenue_less_wages_per_unit": 1.22,
            },
        ],
    },
]

def redis_client():
    r = redis.Redis.from_url(uri_redis)
    return r

def redis_list_push_fifo(list_name, payload, list_max):
    r = redis_client()
    n = r.lpush(list_name, payload)
    t = r.ltrim(list_name, 0, list_max - 1)
    return n

def get_dict_ticker():
    path_log = f"{os.environ['HOME']}/log/gosimcompanies_ticker.log"
    datetime_simco_latest = "unknown"
    dict_ticker = {}
    for line in open(path_log, "r").readlines():
        h = {}
        try:
            h = json.loads(line)
        except Exception as e:
            print(f"JSON PARSE FAILURE: {e}")
        dict_ticker = {t['kind']:t['price'] for t in h['ticker']}
        datetime_simco_latest = f"{h.get('datetime_simco')}"
    return dict_ticker, datetime_simco_latest

def print_stores():
    dict_ticker, datetime_simco_latest = get_dict_ticker()
    print(f"{datetime_simco_latest} [profit per hour, exchange -> retail]")
    for s in stores:
        profit_per_hour = {}
        for k in s['kinds']:
            revenue_per_hour = k['units_sold_per_hour'] * k['revenue_less_wages_per_unit']
            kind = k.get("kind")
            #print({"d": sorted(dict_ticker.keys())})
            if kind in dict_ticker:
                pass
            else:
                print(f"WARNING: name={k.get('name')} kind={kind} not in ticker")
            market_price_per_unit = dict_ticker.get(k.get('kind'), 1000000)
            exchange_cost_to_fill_one_hour = k['units_sold_per_hour'] * market_price_per_unit
            profit_per_hour[k['name']] = round(revenue_per_hour - exchange_cost_to_fill_one_hour, 2)
        d_sorted = dict(sorted(profit_per_hour.items(), key=lambda x: x[1], reverse=True))
        print(f"  {s['name']} {d_sorted}")
