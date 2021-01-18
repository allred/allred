#!/usr/bin/env python
import re
from dateutil import parser # pip install python-dateutil
from pprint import pprint
from tabulate import tabulate
from simco_base import *

rc = redis_client()

k = get_kinds_from_stores()
resources_redis = rc.hgetall("simco:resources")
pattern = re.compile(".*datetime.*")
status = {}
for i in resources_redis:
    num, label = i.decode().split(':')
    if pattern.match(i.decode()):
        status[f"{k[int(num)]}:{num}"] = parser.parse(resources_redis[i].decode()).timestamp()

status_sorted = sorted(status.items(), key=lambda y: str(y[1]), reverse=True)
status_out = []
for k,v in status_sorted:
    status_out.append([k, str(datetime.fromtimestamp(v))])
#pprint(status_out)
print(tabulate(status_out, headers=["resource:num", "last fetched"]))
