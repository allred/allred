#!/usr/bin/env python
import random
from simco_base import *

kinds = get_kinds_from_stores()
kind_random = random.choice(list(kinds.keys()))
print(f"fetching {kind_random}")
r = request_resource_from_api(kind_random)
if r.ok:
    n = redis_hset_resource(kind_random, r.json())
    print(r.json())
    print(f"result: {n}")
else:
    print(r)
