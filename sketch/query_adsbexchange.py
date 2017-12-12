#!/usr/bin/env python
import json
import requests

lat = '40.71284'
lng = '-73.93779'

url_base = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?'
#url_base = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=33.433638&lng=-112.008113&fDstL=0&fDstU=100'

query_params = f'lat={lat}&lng={lng}&fDstL=0&fDstU=100'
query = url_base + query_params 
r = requests.get(query)
json = r.json()
for a in json['acList']:
    call = a.get("Call", "")
    frm = a.get("From", "")
    icao = a.get("Icao", "")
    mdl = a.get("Mdl", "")
    op = a.get("Op", "")
    sql = a.get("Sqk", "")
    to = a.get("To", "")
    output = f'{call} {a["Alt"]} {mdl} {op}'
    #print(a)
    print(output)
