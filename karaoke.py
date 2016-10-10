#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import urllib
import sys
import json


def __srt__(datos):
    for tag in datos:
        for etiqueta, atributos in tag.items():
            linea = etiqueta + "\t"
            for c, v in atributos.items():
                linea = linea + c +"="+ "\""+ v + "\""+"\t" 
            print(linea)
            

def to_json(name_fichero, datos):
    f = name_fichero[:-4] + "json"
    json.dump(datos,open(f,'w'))
    
        
def do_local(datos):
    for dic in datos:
        for tag, atributos in dic.items():
            if 'src' in atributos:
                name = atributos['src']
                if name[:4] == 'http':
                    local = name.split('/')[-1]
                    urllib.request.urlretrieve(name,local)
                    atributos['src'] = local
         
    


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
    __srt__(misdatos)
    to_json(fichero, misdatos)
    do_local(misdatos)
    __srt__(misdatos)
