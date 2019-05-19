#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, time, os, datetime
from lib import keygenerator
from lib import zip
import multiprocessing
import threading


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
parser.add_argument("-k","--key", help="initial password value")

args = parser.parse_args()

testedKey = []
BruteKey = None

def syncBrutes():
    global testedKey, BruteKey
    while True:
        print(testedKey)
        for key in testedKey:
            data = key.get()
            print("Checked %s" % data, end='\r')
            if not data is str:
                testedKey.remove(key)
            else:
                BruteKey = data
                break

if __name__ == "__main__":
    
    if args.version:
        version()

    if not args.file:
        exit("please first specify the archive file location")

    if not os.path.isfile(args.file):
        exit("No such file found")

    startTime = datetime.datetime.now()
    print ("Start Time %s" % str(startTime))


    if args.all:
        generator = keygenerator.Generator()
    else:
        generator = keygenerator.Generator(
            args.useChars,
            args.useNumbers, 
            args.useSpecialChars, 
            args.useSpace)

    path = os.path.dirname(os.path.abspath(args.file))
    path = os.path.join(path, os.path.splitext(os.path.basename(args.file))[0])
    
    if not os.path.exists(path):
        os.makedirs(path)

    pool = multiprocessing.Pool()

    key = args.key
    keylen = 0

    while True:
        key = generator.next(key)

       

        if keylen != len(key):
            keylen = len(key)
            print("Trying a %d-digit password" % keylen)

        p = pool.apply_async(zip.check, args=(args.file, key, path,))
        testedKey.append(p)

        if not BruteKey == None:
            print("password is %s" % BruteKey)
            break
    
    thread = threading.Thread(target = syncBrutes)
    thread.start()
    thread.join()

    endTime = datetime.datetime.now()
    print ("End Time %s" % str(endTime))

    delta = endTime - startTime
    print ("Total time %s" % str(delta))


    