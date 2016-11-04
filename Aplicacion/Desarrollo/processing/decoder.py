# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:39:38 2016

@author: joanteran
"""

class Decoder():
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Decoder, cls).__new__(cls, *args, **kwargs)
        return cls._instance 
    def __init__(self):
       print("Creando decodificador")