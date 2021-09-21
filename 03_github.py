#!/usr/bin/env python

import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments

if __name__ == "__main__":
    url_1 = "https://api.github.com/emaadmanzoor"
    r = requests.get(url_1)
    print(r.status_code)
    print(r.json())
    
    url_2 = "https://api.github.com/users/emaadmanzoor"
    r = requests.get(url_2)
    print(r.status_code)
    print(r.json())
