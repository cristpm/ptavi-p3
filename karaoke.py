#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys

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
    for etiqueta in misdatos:
        linea = etiqueta['etiqueta'] + "\t"
        for c, v in etiqueta.items():
            if c != 'etiqueta':
                linea = linea + c +"="+ "\""+ v + "\""+"\t"
        print(linea)
            
