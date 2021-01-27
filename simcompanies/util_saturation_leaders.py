#!/usr/bin/env python
from pprint import pprint
from simco_base import *

def main():
    rc = redis_client()
    saturations = {}
    labels = {}
    for k,name in get_kinds_from_stores().items():
        json_res = rc.hget("simco:resources", f"{k}:json")
        dict_res = json.loads(json_res)
        retail_modeling = dict_res["retailModeling"]
        if True or k == 60:
            saturations[f"{k}_{name}"] = dict_res['marketSaturation']
            labels[k] = dict_res['marketSaturationLabel']
    ddict_w = sorted(saturations.items(), key=lambda x: x[1], reverse=True)
    pprint(ddict_w)

if __name__ == '__main__':
    main()
