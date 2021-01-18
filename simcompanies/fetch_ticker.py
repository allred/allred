#!/usr/bin/env python
from simco_base import *

if __name__ == '__main__':
    r, uri_ticker = get_dict_ticker_from_api() 
    #print(r.content.decode("utf-8"))
    dict_ticker = r.json()
    dict_out = {
        "ticker": dict_ticker,
        "uri_ticker": uri_ticker,
    }
    json_ticker = json.dumps(dict_out)
    print(json_ticker)
    redis_list_push_fifo(redis_list_ticker, json_ticker, 50)
