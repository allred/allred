#!/usr/bin/env python
import os
import platform
import pprint
import subprocess
from mastodon import Mastodon
#os.environ.set("PYTHONUNBUFFED", 1)


pp = pprint.PrettyPrinter(indent=4)

mastodon = Mastodon(
    access_token = os.environ.get('MASTODON_CLIENT_SECRET'),
    api_base_url = 'https://hachyderm.io'
)
#print(mastodon.__dir__())
#print(mastodon.instance())
#print(mastodon.instance_activity())
#print(mastodon.instance_peers())
#print(sorted(mastodon.instance_peers()))
servlist = mastodon.instance_peers()

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    #command = ['ping', param, '1', host]
    #command = ['nc', '-vz', host, '80']
    command = ['curl', '--max-time', '5', host]
    completedprocess = subprocess.run(command, capture_output=True)
    #completedprocess = subprocess.run(command) == 0
    return completedprocess 


#pp.pprint(sorted(servlist))
if __name__ == "__main__":
    print(f""" <html> <head> <title>List of Mastodon Servers Status</title> <body> """)
    for s in servlist:
        comprocess = ping(s)
        if comprocess.returncode == 0:
            print(f'<div><a href="http://{s}">{s}</a></div>')
    print(f"""</body></html>""")
