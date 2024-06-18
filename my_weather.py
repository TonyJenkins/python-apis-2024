#!/usr/bin/env python3

import json
import requests

from my_ip import get_long_and_lat_from_ipinfo


def build_openweather_url(location):
    from secrets import OPENWEATHER_KEY as api_key

    lat, lon = location

    return f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'


def get_current_conditions(openweather_response):

    response_dict = json.loads(openweather_response)

    return response_dict['weather'][0]['description'].title()


def get_current_temp(openweather_response):

    response_dict = json.loads(openweather_response)

    return response_dict['main']['temp']


if __name__ == '__main__':

    try:
        location = get_long_and_lat_from_ipinfo()

        query = build_openweather_url(location)
        response = requests.get(query).text

        print(f'The current weather at your location is "{get_current_conditions(response)}".')
        print(f'The current temperature at your location is {get_current_temp(response)}C.')

    except (requests.ConnectionError, requests.HTTPError, requests.Timeout,):
        print('Error accessing the IPInfo server.')
