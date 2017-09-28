#!/usr/bin/env python
import json
import pprint
import sys
import unicodedata

from faker import Faker
from twisted.internet import defer, reactor
from twisted.web.client import getPage

fake = Faker()

def getPageUserAgent(*args, **kwargs):
    if 'agent' not in kwargs:
        kwargs['agent'] = fake.firefox() 
    print(kwargs)
    return getPage(*args, **kwargs)

def metaweatherCallback(result):
    data = {
        'length': len(result),
        'content': result[:10],
    }
    print({'metaweather': data})
    #stuff = json.loads(result)
    #print(stuff['consolidated_weather'])
    return data

def yahooCallback(result):
    data = {
        'length': len(result),
        'content': result[:10],
    }
    stuff = json.loads(result)
    print({'yahoo': stuff['query']['results']['channel']['item']['condition']})
    return data

def listCallback(result):
    for isSuccess, data in result:
        if isSuccess:
            print("listCallBack success: {}".format(data))
        else:
            print({'failed': data})

def finish(ign):
    reactor.stop()

def stringify(uni):
    return unicodedata.normalize('NFKD', uni).encode('ascii', 'ignore')

def test():
    url_yahoo = stringify('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22brooklyn%2C%20ny%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
    #url_metaweather = stringify('https://www.metaweather.com/api/location/2459115/')
    url_metaweather = stringify('https://metaweather.com')
    #url_metaweather = stringify('http://google.com')
    #url_metaweather = stringify('https://mikeallred.com')
    list_deferred = []
    d1 = getPageUserAgent(url_yahoo)
    d1.addCallback(yahooCallback)
    list_deferred.append(d1)
    d2 = getPageUserAgent(url_metaweather)
    d2.addCallback(metaweatherCallback)
    list_deferred.append(d2) 
    dl = defer.DeferredList(list_deferred)
    dl.addCallback(listCallback)
    dl.addCallback(finish)

test()
reactor.run()
