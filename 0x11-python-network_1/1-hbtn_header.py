#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST
    request to the passed URL with the email as a parameter, and
    displays the body of the response (decoded in utf-8)
    You must use the packages urllib and sys
    You are not allow to import packages other than urllib and sys
    The value of this variable is different for each request
    You don’t need to check arguments passed to the script (number or type)
    You must use a with statement
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers['X-Request-Id'])
