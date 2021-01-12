#!/usr/bin/env python
import requests
from datetime import datetime

uri_player = "https://www.simcompanies.com/api/v2/players/me/"
uri_resource_60 = "https://www.simcompanies.com/api/v2/market/60"
uri_ticker = "https://www.simcompanies.com/api/v1/market-ticker/2021-01-11T03:16:43.003Z/"
uri_ticker_base = "https://www.simcompanies.com/api/v1/market-ticker/"

if __name__ == '__main__':
    datetime_now = datetime.now()
    datetime_simco = datetime_now.strftime('%Y-%m-%dT%H:%M:%S.000')
    uri_ticker = f'{uri_ticker_base}{datetime_simco}Z/'
    r = requests.get(uri_ticker)
    print(r.content.decode("utf-8"))
    #print(r.json())
