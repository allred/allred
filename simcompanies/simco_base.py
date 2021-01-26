#!/usr/bin/env python
# [SIMCO BASE]
# ALL YOUR OCMIS ARE BELONG TO US
import json
import logging
import os
import re
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

silog = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
)

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
            "name": "gas",
            "kinds": [
                {
                    "name": "petrol",
                    "kind": 11,
                    "units_sold_per_hour": 82.42,
                    "revenue_less_wages_per_unit": 41.10,
                    },
                {
                    "name": "diesel",
                    "kind": 12,
                    "units_sold_per_hour": 79.52,
                    "revenue_less_wages_per_unit": 40.83,
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
                    "name": "tablets",
                    "kind": 25,
                    "units_sold_per_hour": .56,
                    "revenue_less_wages_per_unit": 836.65,
                    },
                {
                    "name": "laptops",
                    "kind": 26,
                    "units_sold_per_hour": .78,
                    "revenue_less_wages_per_unit": 1256.95,
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
                {
                    "name": "quadcopter",
                    "kind": 98,
                    "units_sold_per_hour": .7,
                    "revenue_less_wages_per_unit": 937.64,
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
                        "name": "dress",
                        "kind": 62,
                        "units_sold_per_hour": 40.12,
                        "revenue_less_wages_per_unit": 19.16,
                        },
                    {
                        "name": "heels",
                        "kind": 63,
                        "units_sold_per_hour": 25.74,
                        "revenue_less_wages_per_unit": 22.53,
                        },
                    {
                        "name": "handbags",
                        "kind": 64,
                        "units_sold_per_hour": 15.52,
                        "revenue_less_wages_per_unit": 28.38,
                        },
                    {
                        "name": "sneakers",
                        "kind": 65,
                        "units_sold_per_hour": 26.08,
                        "revenue_less_wages_per_unit": 16.81,
                        },
                    {
                        "name": "lux_watch",
                        "kind": 70,
                        "units_sold_per_hour": 2.33,
                        "revenue_less_wages_per_unit": 757.96,
                        },
                    {
                        "name": "necklace",
                        "kind": 71,
                        "units_sold_per_hour": 1.28,
                        "revenue_less_wages_per_unit": 1497.97,
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
                    "units_sold_per_hour": 63.42,
                    "revenue_less_wages_per_unit": 2.24,
                    },
                {
                    "name": "grapes",
                    "kind": 5,
                    "units_sold_per_hour": 63.19,
                    "revenue_less_wages_per_unit": 2.73,
                    },
                {
                    "name": "steak",
                    "kind": 7,
                    "units_sold_per_hour": 20.76,
                    "revenue_less_wages_per_unit": 11.76,
                    },
                {
                    "name": "eggs",
                    "kind": 9,
                    "units_sold_per_hour": 290.79,
                    "revenue_less_wages_per_unit": 1.21,
                    },
                {
                    "name": "sausages",
                    "kind": 8,
                    "units_sold_per_hour": 80.41,
                    "revenue_less_wages_per_unit": 3.90,
                    },
                ],
            },
    ]

class Simco:
    def silog(msg):
        """ breakfast style logging """
        logging.warning(msg)

def print_stores():
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
        if len(kinds_not_found) > 0:
            logging.warning(f"WARNING: {len(kinds_not_found)} not in ticker")
        profit_per_hour[k['name']] = round(revenue_per_hour - exchange_cost_to_fill_one_hour, 2)
        d_sorted = dict(sorted(profit_per_hour.items(), key=lambda x: x[1], reverse=True))
        print(f"  [{s['name'].upper()}] {d_sorted}")


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

def get_dict_ticker_from_log():
    path_log = f"{os.environ['HOME']}/log/simco_cron_fetch_ticker.log"
    datetime_simco_latest = "unknown"
    dict_ticker = {}
    line_count = 0
    fh = open(path_log, "r")
    found_json_in_file = False
    datetime_simco_latest = 'UNKNOWN'
    for line in fh.readlines():
        if found_json_in_file:
            break
        h = {"ticker": []}
        try:
            h = json.loads(line)
            dict_ticker = {t['kind']:t['price'] for t in h['ticker']}
            datetime_simco_latest = h.get("uri_ticker").split("/")[-2]
            found_json_in_file = True
        except Exception as e:
            #logging.debug(f"json parse failure: {e} path_log: {path_log}")
            #logging.debug(f"line: {line}")
            #logging.debug(line)
            pass
    if not found_json_in_file:
        logging.debug(f"read: {fh} {path_log}")
    return dict_ticker, datetime_simco_latest

def request_dict_ticker_from_simco_http():
    datetime_now = datetime.now()
    datetime_simco = datetime_now.strftime('%Y-%m-%dT%H:%M:%S.000')
    uri_ticker = f'{uri_api_ticker_base}{datetime_simco}Z/'
    r = requests.get(uri_ticker)
    if r.ok:
        return r, uri_ticker
    else:
        print(f"failure: {r}")

def retail_modeling_calculate(group_dict, price, saturation, amount=1):
    """ example: (Math.pow(price*2.995075 + (-7.061656 + (saturation - 0.5)/0.455885), 2.000000)*0.748513 + 20.189612)*amount """
    n1 = group_dict.get("num1")
    n2 = group_dict.get("num2")
    n3 = group_dict.get("num3")
    n4 = group_dict.get("num4")
    n5 = group_dict.get("num5")
    n6 = group_dict.get("num6")
    exp = group_dict.get("exponent")
    units_per_hour = ((price*n1 + (n2 + (saturation - n3)/n4))**exp * n5 + n6)*amount
    return units_per_hour

def retail_modeling_parse(model):
    """ example: (Math.pow(price*2.995075 + (-7.061656 + (saturation - 0.5)/0.455885), 2.000000)*0.748513 + 20.189612)*amount """
    re_model = re.compile(r'''
        ^.*?
        (?P<num1>\d+\.\d+)
        .*?(?P<num2>-*\d+\.\d+)
        .*?(?P<num3>-*\d+\.\d+)
        .*?(?P<num4>-*\d+\.\d+)
        .*?(?P<exponent>-*\d+\.\d+)
        .*?(?P<num5>-*\d+\.\d+)
        .*?(?P<num6>-*\d+\.\d+)
        .*
    ''', re.VERBOSE)
    m = re_model.search(model)
    group_dict = m.groupdict()
    assert len(group_dict.values()) == 7
    return {k:float(v) for k,v in m.groupdict().items()}


def get_kinds_from_stores():
    kinds = {}
    for s in stores:
        for k in s.get("kinds"):
            kinds[k.get("kind")] = k.get("name")
    return kinds
