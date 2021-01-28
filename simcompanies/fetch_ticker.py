#!/usr/bin/env python
import os
from simco_base import *
from simco_influxdb import *

def push_to_redis():
    redis_list_push_fifo(redis_list_ticker, json_ticker, 50)

def write_to_influxdb():
    bucket = "mikejallred's Bucket"
    client = influxdb_client()
    write_api = client.write_api(write_options=SYNCHRONOUS)
    for r in list_ticker:
        influx_line = f'ticker,kind={r["kind"]} price={r["price"]}'
        ir = write_api.write(bucket, org_influxdb, influx_line)

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
    print("")
    print(json_ticker)
    print("")
    logging.error(" ")
    os.system('echo ""')

    logging.debug("pushing to redis")
    try:
        push_to_redis()
    except Exception as e:
        print(e)

    logging.debug("pushing to influxdb")
    try:
        write_to_influxdb()
    except Exception as e:
        print(e)

    logging.debug("done")
    print(json_ticker)
