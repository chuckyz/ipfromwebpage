#!/usr/bin/env python3

__author__ = 'Jay Shepherd'

import re
from urllib.parse import urlparse
from urllib.request import urlopen

import bs4


def interactive_url_input():
    """
    :return: Printed result of URL scrape
    """
    url_input = ''
    while not validate_url(url_input):
        url_input = input("Please enter a url to scrape for IPs. The URL must include http:// or https://: ")
        print('')
    return url_input


def validate_url(url_arg):
    """ Takes string input and validates if it is fully qualified url for passing into other functions
    :param url_arg: URL to check for validation
    :return: Boolean result of validation check
    """
    return urlparse(url_arg).scheme is not ''


def get_webpage_text(url_input):
    """
    Extracts text of webpage and returns
    :param url_input: Fully-qualified URL to scrape for IP Addresses
    :return: Text of webpage
    """
    data = bs4.BeautifulSoup(urlopen(url_input), 'html.parser')
    return str(data.get_text)


def ip_from_string(string):
    """
    Takes a string and extracts all IP Addresses as a SET
    :param string: Any string of data
    :return: IP Addresses as a SET
    """
    ip_address = re.compile('(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?:\/[0-9]{1,2})?')
    return set(ip_address.findall(string))


def main():
    try:
        url_input = interactive_url_input()
        webpage_text = get_webpage_text(url_input)
        address_list = ip_from_string(webpage_text)
        if address_list:
            print("\n".join(address_list))
        else:
            print("No ips found when scraping {}".format(url_input))
    except KeyboardInterrupt:
        print("\nGoodbye")


if __name__ == '__main__':
    main()
