#!/usr/bin/env python
import json
import os
import sys
from simco_base import *

path_log = f"{os.environ['HOME']}/log/gosimcompanies_ticker.log"
datetime_simco_latest = "unknown"
dict_ticker = {}
for line in open(path_log, "r").readlines():
    h = {}
    try:
        h = json.loads(line)
    except Exception as e:
        print(f"JSON PARSE FAILURE: {e}")
        continue
    dict_ticker = {t['kind']:t['price'] for t in h['ticker']}
    datetime_simco_latest = f"{h.get('datetime_simco')}"

print(f"{datetime_simco_latest} [profit per hour, exchange -> retail]")
print_stores()
