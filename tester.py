#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from zipfile import ZipFile
from threading import Thread

def check(zFile, password):
    try:
        zFile.extractall(pwd=bytes(password,'utf-8'))
        return True
    except Exception as ex:
        print(ex)
        return False


zFile = ZipFile("./test.rar")
print(check(zFile,"abcd"))