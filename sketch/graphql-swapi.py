#!/usr/bin/env python
# https://github.com/graphql/swapi-graphql/tree/master/doc/example_queries
#import graphene
import requests
import pprint

pp = pprint.PrettyPrinter()
uri = 'https://api.graphcms.com/simple/v1/swapi'
data = {
        "query": '''{
            Person(name: "Luke Skywalker") {
                name
                height
                gender
                homeworld {
                    name
                }
                films {
                    title 
                }
            }
        }''',
        }
r = requests.post(uri, json=data)
#print(r.headers)
#print(r.text)
pp.pprint(r.json())
