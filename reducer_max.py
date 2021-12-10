#!/usr/bin/env python3

import sys

def reducer():
    salesmax = 0
    oldKey = None

    for line in sys.stdin:
        data = line.strip().split(",")

        thisKey, thisCost = data
        if oldKey is not None and oldKey != thisKey:
            print(oldKey + "," + str(salesmax))
            salesmax = 0

        oldKey = thisKey
        sales = float(thisCost)
        salesmax = max(salesmax, sales)

    if oldKey is not None: # for the final key
        print (oldKey + "," + str(salesmax))

if __name__ == "__main__":
    # what function should run when python reducer.py is called?
    reducer()
