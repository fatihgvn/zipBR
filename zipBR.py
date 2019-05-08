#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, time
from lib import keygenerator

parser = argparse.ArgumentParser()

parser.add_argument("-f","--file", help="Location of the archive to open")
# parser.add_argument("-l","--localhost", help="server run localhost", action="store_true")

args = parser.parse_args()

if __name__ == "__main__":
    # try:
        
    generator = keygenerator.Generator()
    key = None
    while True:
        key = generator.next(key)
        print(key)
        time.sleep(0.2)


    # except Exception as ex:
    #     print(ex)