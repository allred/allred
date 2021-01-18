#!/usr/bin/env python
import json
import os
import redis
import requests
from datetime import datetime

token_redis = os.environ["SIMCO_REDIS_TOKEN"]
uri_redis = f"redis://{token_redis}@redis-10827.c8.us-east-1-4.ec2.cloud.redislabs.com:10827"
redis_list_ticker = "simco:ticker_json"
redis_list_resource_apples = "simco:resource_apples_json"

uri_api_base_v1 = "https://www.simcompanies.com/api/v1"
uri_api_ticker_base = f"{uri_api_base_v1}/market-ticker/"
uri_player = "https://www.simcompanies.com/api/v2/players/me/"
uri_resource_60 = "https://www.simcompanies.com/api/v2/market/60"

# get these values from the Encyclopedia
stores = [
    {
        "name": "car_dealership",
        "kinds": [
            {
                "name": "economy_car",
                "kind": 55,
                "units_sold_per_hour": 1.63,
                "revenue_less_wages_per_unit": 2271.38,
            },
            {
                "name": "economy_e_car",
                "kind": 53,
                "units_sold_per_hour": 1.30,
                "revenue_less_wages_per_unit": 3393.78,
            },
            {
                "name": "truck",
                "kind": 57,
                "units_sold_per_hour": 0.66,
                "revenue_less_wages_per_unit": 5696.20,
            },
        ],
    },
    {
        "name": "electronics",
        "kinds": [
            {
                "name": "smart_phones",
                "kind": 24,
                "units_sold_per_hour": 1.57,
                "revenue_less_wages_per_unit": 650.11,
            },
            {
                "name": "monitors",
                "kind": 27,
                "units_sold_per_hour": 1.28,
                "revenue_less_wages_per_unit": 574.46,
            },
            {
                "name": "tvs",
                "kind": 28,
                "units_sold_per_hour": 1.37,
                "revenue_less_wages_per_unit": 953.78,
            },
        ],
    },
    {
        "name": "fashion",
        "kinds": [
            {
                "name": "underwear",
                "kind": 60,
                "units_sold_per_hour": 23.00,
                "revenue_less_wages_per_unit": 8.03,
            },
            {
                "name": "gloves",
                "kind": 61,
                "units_sold_per_hour": 16.90,
                "revenue_less_wages_per_unit": 16.10,
            },
            {
                "name": "sneakers",
                "kind": 65,
                "units_sold_per_hour": 26.08,
                "revenue_less_wages_per_unit": 16.81,
            },
        ],
    },
    {
        "name": "hardware",
        "kinds": [
            {
                "name": "bricks",
                "kind": 102,
                "units_sold_per_hour": 75.85,
                "revenue_less_wages_per_unit": 3.50,
            },
            {
                "name": "cement",
                "kind": 103,
                "units_sold_per_hour": 55.22,
                "revenue_less_wages_per_unit": 7.35,
            },
            {
                "name": "planks",
                "kind": 108,
                "units_sold_per_hour": 99.09,
                "revenue_less_wages_per_unit": 10.04,
            },
        ],
    },
    {
        "name": "grocery",
        "kinds": [
            {
                "name": "apples",
                "kind": 3,
                "units_sold_per_hour": 85.84,
                "revenue_less_wages_per_unit": 2.18,
            },
            {
                "name": "oranges",
                "kind": 4,
                "units_sold_per_hour": 64.94,
                "revenue_less_wages_per_unit": 2.27,
            },
            {
                "name": "eggs",
                "kind": 9,
                "units_sold_per_hour": 290.79,
                "revenue_less_wages_per_unit": 1.21,
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

def redis_hset_resource(resource_num, payload):
    r = redis_client()
    n = r.hmset("simco:resources", {
        f"{resource_num}:json": json.dumps(payload),
        f"{resource_num}:datetime": str(datetime.now()),
    })
    return n

def request_resource_from_api(resource_num):
    uri = f"https://www.simcompanies.com/api/v3/en/encyclopedia/resources/1/{resource_num}/"
    r = requests.get(uri)
    return r

def get_dict_ticker():
    path_log = f"{os.environ['HOME']}/log/simco_cron_fetch_ticker.log"
    datetime_simco_latest = "unknown"
    dict_ticker = {}
    for line in open(path_log, "r").readlines():
        h = {}
        try:
            h = json.loads(line)
        except Exception as e:
            print(f"JSON PARSE FAILURE: {e}")
        dict_ticker = {t['kind']:t['price'] for t in h['ticker']}
        datetime_simco_latest = h.get("uri_ticker").split("/")[-2]
    return dict_ticker, datetime_simco_latest

def get_dict_ticker_from_api():
    datetime_now = datetime.now()
    datetime_simco = datetime_now.strftime('%Y-%m-%dT%H:%M:%S.000')
    uri_ticker = f'{uri_api_ticker_base}{datetime_simco}Z/'
    r = requests.get(uri_ticker)
    if r.ok:
        return r, uri_ticker
    else:
        print(f"failure: {r}")

def parse_retail_modeling(model):
    print(model)

def print_stores():
    dict_ticker, datetime_simco_latest = get_dict_ticker()
    print(f"{datetime_simco_latest} [profit per hour, exchange -> retail]")
    for s in stores:
        profit_per_hour = {}
        for k in s['kinds']:
            revenue_per_hour = k['units_sold_per_hour'] * k['revenue_less_wages_per_unit']
            kind = k.get("kind")
            if not kind in dict_ticker:
                print(f"WARNING: name={k.get('name')} kind={kind} not in ticker")
            market_price_per_unit = dict_ticker.get(k.get('kind'), 1000000)
            exchange_cost_to_fill_one_hour = k['units_sold_per_hour'] * market_price_per_unit
            profit_per_hour[k['name']] = round(revenue_per_hour - exchange_cost_to_fill_one_hour, 2)
        d_sorted = dict(sorted(profit_per_hour.items(), key=lambda x: x[1], reverse=True))
        print(f"  {s['name']} {d_sorted}")

def get_kinds_from_stores():
    kinds = {}
    for s in stores:
        for k in s.get("kinds"):
            kinds[k.get("kind")] = k.get("name") 
    return kinds
