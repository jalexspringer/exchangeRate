'''
API wrapper for the openexchangerates.org currency exchange rate API and ipinfo.io IP information API.
The exchanger class utilizes the free openexchangerates account tier, gets the USD exchange rates, and derives global exchange rates between all currencies from there.
An API key is required for openexchangerates when this class is initialized.

The userVisit class is intended for use in a web app - it automaticall captures the user IP and uses the ipinfo.io API to find the country the IP is listed as from.

An API key is required for ipinfo.io when this class is initialized.
'''

import requests
import json
import re
import csv

from .country_currency import codes_to_currencies_dict
from .currency_code import currency_codes_dict


class exchanger():
    def __init__(self, access_key):
        self.access_key = access_key
        self.base_currency = 'USD'
        self.currencies = self.currencyCode()
        self.base_rates = self.getExRate()
        self.all_rates_dict = self.getAllRates()
        self.all_rates_list = self.createListofDicts()

    def currencyCode(self):
        # Get current list of currencies and currency codes
        base_url = 'https://openexchangerates.org/api/currencies.json?'
        access_key = 'app_id={}'.format(self.access_key)
        complete_url = base_url + access_key
        response = requests.get(complete_url)
        return response.json()

    def getExRate(self):
        # List of current exchange rates against the base currency. Default USD
        base_url = 'https://openexchangerates.org/api/latest.json?'
        access_key = 'app_id={}'.format(self.access_key)
        if self.base_currency =='USD':
            complete_url = base_url + access_key
        else:
            base_currency = '&base={}'.format(self.base_currency)
            complete_url = base_url + access_key + self.base_currency
        response = requests.get(complete_url)
        return response.json()

    def getAllRates(self):
        # Use the USD conversion rates to get all rates between all currencies.
        new_dict = {}
        for k,v in self.base_rates['rates'].items():
            new_dict[k]= {'USD': 1/v}
        for k,v in new_dict.items():
            for currency in self.base_rates['rates']:
                new_dict[k].update({currency: v['USD'] * self.base_rates['rates'][currency]})
        return new_dict
    
    def createListofDicts(self)
        all_rates = []
        for k,v in self.all_rates_dict.items():
            all_rates.append({'_id': k, 'rates': v})
        return all_rates


class userVisit():
    def __init__(self, access_key, ip=None):
    # Uncomment the line below and comment out the one above to hardcode an IP for testing.
    # def __init__(self, access_key, ip='178.249.14.12'):
        self.ip = ip
        self.access_key = access_key
        self.conversion_dict = codes_to_currencies_dict
        self.currency_dict = currency_codes_dict
        self.country = self.countryFromIP()
        try:
            self.currency = self.conversion_dict[self.country]
        except KeyError:
            self.currency = 'USD'
        try:
            self.currency_long = self.currency_dict[self.currency]
        except KeyError:
            self.currency_long = 'United States Dollar'

    def countryFromIP(self):
        # Get the user's country
        if self.ip:
            base_url = 'http://ipinfo.io/{}/json'.format(self.ip)
        else:
            base_url = 'http://ipinfo.io/json'
        response = requests.get(base_url)
        return response.json()['country']
