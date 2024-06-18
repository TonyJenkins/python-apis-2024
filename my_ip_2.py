#!/usr/bin/env python3

import ipinfo
import requests


def ipinfo_query():
    from secrets import IPINFO_KEY

    return ipinfo.getHandler(access_token=IPINFO_KEY).getDetails()


def get_location_from_ipinfo(ip_info):

    return ip_info.city


def get_long_and_lat_from_ipinfo(ip_info):

    return tuple(ip_info.loc.split(','))


if __name__ == '__main__':

    try:
        facts = ipinfo_query()

        print(f'Your current IP address is {facts.ip}, which is probably located in {facts.city}.')
    except (requests.ConnectionError, requests.HTTPError, requests.Timeout,):
        print('Error accessing the IPInfo server.')
