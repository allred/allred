#!/usr/bin/env python
# probe some stuff
import inspect
import os
import platform
import pprint
import requests
import subprocess
from mastodon import Mastodon


pp = pprint.PrettyPrinter(indent=4)

mastodon = Mastodon(
    access_token = os.environ.get('MASTODON_CLIENT_SECRET'),
    api_base_url = 'https://hachyderm.io'
)

def probemeister(host):
    #pp.pprint(mastodon.instance_nodeinfo())
    url = f"https://{host}/v2/instance"
    #url = f"https://{host}/v1/instance"
    pp.pprint(url)
    r = requests.get(url)
    return r.status_code


if __name__ == "__main__":
    #pp.pprint(dir(mastodon))
    #pp.pprint(mastodon.instance_nodeinfo())
    servlist = mastodon.instance_peers()
    itercount = 0
    for s in servlist:
        pp.pprint(s)
        r = probemeister(s)
        pp.pprint(r)
        itercount += 1
        if itercount >= 3:
            break 
    #pp.pprint(servlist)
