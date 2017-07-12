#!/usr/bin/env python
# ideas:
# - use grubhub menus, menupages is derelict
# - cache per-zip code data for at least a day
# - perimeterx bot js/cookie setup would need to be dealt with
# - proxy chrome-headless through a user-agent modifier
# https://api-gtm.grubhub.com/restaurants/325255?hideChoiceCategories=true&hideUnavailableMenuItems=true&hideMenuItems=true&showMenuItemCoupons=true&location=POINT(-73.95655823%2040.70933532)
import bs4
import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
  'User-Agent': ua.ff,
}
jar = requests.cookies.RequestsCookieJar()
session = requests.Session()

def req(url):
  #r = requests.get(url, headers=headers)
  #return s.get(url, headers=headers, cookies=jar)
  return session.get(url, headers=headers)


def scrape(url):
  r = req(url)
  print(r.text)
  print(r.headers)
  print(r.status_code)

if __name__ == '__main__':
  url = 'http://www.menupages.com/restaurants/adv/___11211/all-areas/all-neighborhoods/all-cuisines/'
  url = 'http://mikeallred.com'
  url = 'https://api-gtm.grubhub.com/restaurants/325255?hideChoiceCategories=true&hideUnavailableMenuItems=true&hideMenuItems=true&showMenuItemCoupons=true&location=POINT(-73.95655823%2040.70933532)'
  print(req('http://grubhub.com').headers)
  print(session.cookies)
  scrape(url)

