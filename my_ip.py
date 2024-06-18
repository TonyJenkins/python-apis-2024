#!/usr/bin/env python3

import json
import requests


def build_query_url():
    from secrets import IPINFO_KEY

    return f'https://ipinfo.io/json?token={IPINFO_KEY}'


if __name__ == '__main__':

    try:
        response = requests.get(build_query_url())
        facts = json.loads(response.text)

        print(f'Your current IP address is {facts['ip']}, which is probably located in {facts['city']}.')
    except (requests.ConnectionError, requests.HTTPError, requests.Timeout,):
        print('Error accessing the IPInfo server.')
