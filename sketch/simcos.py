#!/usr/bin/env python
import requests

uri_player = "https://www.simcompanies.com/api/v2/players/me/"
r = requests.get(uri_player)
print(r)
