#!/usr/bin/env python
# probe some stuff
import inspect
import os
import platform
import pprint
import subprocess
from mastodon import Mastodon


pp = pprint.PrettyPrinter(indent=4)

mastodon = Mastodon(
    access_token = os.environ.get('MASTODON_CLIENT_SECRET'),
    api_base_url = 'https://hachyderm.io'
)

if __name__ == "__main__":
    pp.pprint(dir(mastodon))
    pp.pprint(mastodon.instance_nodeinfo())
    #servlist = mastodon.instance_peers()
    #pp.pprint(servlist)
