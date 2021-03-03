#!/usr/bin/env python
# [SIMCO BASE]
# ALL YOUR OCMIS ARE BELONG TO US
import json
import logging
import os
import re
import redis
import requests
from collections import defaultdict
from datetime import datetime, timedelta
from simco_stores import stores

token_redis = os.environ["SIMCO_REDIS_TOKEN"]
hostport_redis = os.environ["SIMCO_REDIS_URI"]
uri_redis = f"redis://:{token_redis}@{hostport_redis}"
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

class Simco:
    def silog(msg):
        """ breakfast style logging """
        logging.warning(msg)

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
            #logging.debug(f"json parse result: {h}")
            dict_ticker = {t['kind']:t['price'] for t in h['ticker']}
            datetime_simco_latest = h.get("uri_ticker").split("/")[-2]
            found_json_in_file = True
        except Exception as e:
            #logging.debug(f"json parse failure: error:{e} path_log:{path_log} line:{line}")
            pass
    if found_json_in_file is not True:
        logging.debug(f"didn't find json in file")
        logging.debug(f"read: {fh} {path_log}")
    return dict_ticker, datetime_simco_latest

def request_dict_ticker_from_simco_http():
    # date needs to be slightly in the past
    minutes_in_the_past = 80
    datetime_past = datetime.now() - timedelta(minutes=minutes_in_the_past)
    datetime_simco = datetime_past.strftime('%Y-%m-%dT%H:%M:%S.000')
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
