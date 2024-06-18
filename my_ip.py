#!/usr/bin/env python3

import json
import requests


def build_query_url():
    from secrets import IPINFO_KEY

    return f'https://ipinfo.io/json?token={IPINFO_KEY}'


def get_all_from_ipinfo():

    response = requests.get(build_query_url())
    facts_dict = json.loads(response.text)

    return facts_dict


def get_location_from_ipinfo():

    return get_all_from_ipinfo()['city']


def get_long_and_lat_from_ipinfo():

    location = get_all_from_ipinfo()['loc']

    return tuple(location.split(','))


if __name__ == '__main__':

    try:
        facts = get_all_from_ipinfo()

        print(f'Your current IP address is {facts['ip']}, which is probably located in {facts['city']}.')
    except (requests.ConnectionError, requests.HTTPError, requests.Timeout,):
        print('Error accessing the IPInfo server.')
