#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import json

def imprimir_tags(datos):
    for tag in datos:
        for etiqueta, atributos in tag.items():
            linea = etiqueta + "\t"
            for c, v in atributos.items():
                linea = linea + c +"="+ "\""+ v + "\""+"\t" 
            print(linea)

def file_json(name_fichero, datos):
    f = name_fichero[:-4] + "json"
    f = open(f, 'w')
    for d in misdatos:
        json.dump(d, f)

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python3 karaoke.py file.smil.')
        
    parser.parse(open(fichero))
    misdatos = cHandler.get_tags()
    imprimir_tags(misdatos)
    file_json(fichero, misdatos)
