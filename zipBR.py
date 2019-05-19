#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, time, os, datetime
from lib import keygenerator
from lib import zip
from multiprocessing import Pool


def version():
    major = 1
    minor = 0
    rev = 0
    build = 1 
    buildtime = "16:05 17.05.2019"
    print("Program Version %d.%d.%d.%d" % (major, minor, rev, build))
    print("Build Time %s" % (buildtime))
    exit(0)

parser = argparse.ArgumentParser()

parser.add_argument("-f","--file", help="Location of the archive to open")
parser.add_argument("-a","--all", help="Use any chars", action="store_true")
parser.add_argument("-c","--useChars", help="Use all letters from a to Z", action="store_true")
parser.add_argument("-n","--useNumbers", help="Use all figures", action="store_true")
parser.add_argument("-s","--useSpecialChars", help="Use special characters", action="store_true")
parser.add_argument("-p","--useSpace", help="Use <SPACE> character", action="store_true")
parser.add_argument("-v","--version", help="Show version number", action='store_true')

args = parser.parse_args()


if __name__ == "__main__":
    
    if args.version:
        version()

    if not args.file:
        exit("please first specify the archive file location")


    try:

        if not os.path.isfile(args.file):
            exit("No such file found")

        if args.all:
            generator = keygenerator.Generator()
        else:
            generator = keygenerator.Generator(
                args.useChars,
                args.useNumbers, 
                args.useSpecialChars, 
                args.useSpace)

        key = None
        keylen = 0

        path = os.path.dirname(os.path.abspath(args.file))
        path = os.path.join(path, os.path.splitext(os.path.basename(args.file))[0])
        
        if not os.path.exists(path):
            os.makedirs(path)

        startTime = datetime.datetime.now()

        print ("Start Time %s" % str(startTime))
        
        while True:
            with Pool() as pool:
                key = generator.next(key)

                print("Checked %s" % key, end='\r')

                if keylen != len(key):
                    keylen = len(key)
                    print("Trying a %d-digit password" % keylen)

                ret = pool.apply(zip.check, (args.file, key, path))

                if ret:
                    print("password is %s" % key)
                    break


        endTime = datetime.datetime.now()
        print ("End Time %s" % str(endTime))

        delta = endTime - startTime
        print ("Total time %s" % str(delta))


    except KeyboardInterrupt:
        pass