#!/usr/bin/env python

import json # to parse JSON
import requests # to make HTTP requests
import argparse # to parse command-line arguments
import time

if __name__ == "__main__":
    url_1 = "https://api.github.com/emaadmanzoor"
    r = requests.get(url_1)
    print(r.status_code)
    print(r.json())
    
    url_2 = "https://api.github.com/users/emaadmanzoor"
    r = requests.get(url_2)
    print(r.status_code)

    for key, value in r.json().items():
        print(key, value)

    print(r.headers)

    reset_time = r.headers["x-ratelimit-reset"]
    print("Rate limit resets at:", reset_time)

    remaining = r.headers["x-ratelimit-remaining"]
    print("API calls remaining:", remaining)

    current_time = time.time()
    reset_time = int(reset_time) # the API gives you a string, not an integer
    remaining_time = reset_time - current_time
    print("Remaining time (seconds)",
            remaining_time)

    print("Sleeping until reset...")
    time.sleep(remaining_time)
