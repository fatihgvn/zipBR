#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from zipfile import ZipFile

def check(name, password, folder):
    try:
        with ZipFile(name) as zf:
            zf.extractall(path=folder, pwd=bytes(password,'utf-8'))
            return True
    except:
        return False