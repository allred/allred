#!/usr/bin/env python
# stdout and stdin alternate, so beware
import os
from simco_base import *
from simco_influxdb import *

def push_to_redis():
    redis_list_push_fifo(redis_list_ticker, json_ticker, 50)

def write_to_influxdb():
    bucket = "mikejallred's Bucket"
    client = influxdb_client()
    write_api = client.write_api(write_options=SYNCHRONOUS)
    list_write_to_influx = []
    for r in list_ticker:
        influx_line = f'ticker,kind={r["kind"]} price={r["price"]}'
        list_write_to_influx.append(influx_line)
    res_write = write_api.write(bucket, org_influxdb, list_write_to_influx)
    return res_write

if __name__ == '__main__':
    r, uri_ticker = request_dict_ticker_from_simco_http() 
    #print(r.content.decode("utf-8"))
    list_ticker = r.json()
    dict_out = {
        "ticker": list_ticker,
        "uri_ticker": uri_ticker,
    }
    json_ticker = json.dumps(dict_out)

    os.system('echo ""')
    print(json_ticker)
    print("")
    print(json_ticker)
    print("")
    os.system('>&2 echo ""')
    logging.info(" ")

    logging.debug("redis push")
    try:
        res_red = push_to_redis()
    except Exception as e:
        print(e)
    logging.debug(f"redis push done: {res_red}")

    logging.debug("influxdb write start")
    try:
        res_inf = write_to_influxdb()
    except Exception as e:
        print(e)
    logging.debug(f"influxdb write done: {res_inf}")
