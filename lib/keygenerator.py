#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Generator:
    
    charSet = None
    lastedSet = None

    def __init__(self, useChars = True, useNumbers = True, useSpecialChars = True, useSpace = True):
        import string

        if useChars:
            self.charSet = string.ascii_letters
        if useNumbers:
            self.charSet += str(string.digits)
        if useSpecialChars:
            self.charSet += string.punctuation
        if useSpace:
            self.charSet += ' '

        if useChars == False and useNumbers == False and useSpecialChars == False and useSpace == False:
            exit("Character list cannot be empty")

        print("Using char list is:")
        print(self.charSet)

        self.lastedSet = self.charSet[len(self.charSet) - 1]

    def next(self, old = None):
        if old == None:
            return self.charSet[0]
        else:
            length = len(old) # eski metnin uzunluğunu bulduk
            char = length - 1 # son karakterin indexini aldık

            _old = list(old) # metni karakter listesi haline getirdik


            if _old[char] != self.lastedSet:
                index = self.charSet.index(_old[char]) + 1
                _old[char] = self.charSet[index]
            else:
                if char == 0:
                    _old[char] = self.charSet[0]
                    _old = [self.charSet[0]] + _old
                else: 
                    _old[char] = self.charSet[0]
                    while True:
                        char-=1
                        if _old[char] != self.lastedSet:
                            index = self.charSet.index(_old[char]) + 1
                            _old[char] = self.charSet[index]
                            break
                        else:
                            _old[char] = self.charSet[0]
                            if char == 0:
                                _old = [self.charSet[0]] + _old

            return "".join(_old)