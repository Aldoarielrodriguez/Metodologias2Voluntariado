# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:39:38 2016

@author: joanteran
"""


url = "/home/semperti/joan/cosa/archivo.epa"
print("print(url)")
print(url)

def obtenerNombre(url):
    nombre = url.split("/")
    nombre = nombre[len(nombre)-1]
    print nombre
    
obtenerNombre(url)