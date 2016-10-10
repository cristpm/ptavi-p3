#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import urllib
import sys
import json

try:
    fichero = sys.argv[1]
except IndexError:
    sys.exit('Usage: python3 karaoke.py file.smil.')
    
fich_json = fichero[:-4] + "json"

class KaraokeLocal():

    def __init__ (self, fichero):
        parser = make_parser()
        self.cHandler = SmallSMILHandler()
        parser.setContentHandler(self.cHandler)
        parser.parse(open(fichero))
        self.misdatos = self.cHandler.get_tags()
        
    def __srt__(self):
        for tag in self.misdatos:
            for etiqueta, atributos in tag.items():
                linea = etiqueta + "\t"
                for c, v in atributos.items():
                    linea = linea + c +"="+ "\""+ v + "\""+"\t" 
                print(linea)
                
    def to_json(self, f, f_json = fich_json):
        json.dump(self.misdatos,open(f_json,'w'))
        
    def do_local(self):
        for dic in self.misdatos:
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
    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python3 karaoke.py file.smil.')
    
    karaoke = KaraokeLocal(fichero)
    karaoke.__srt__()
    karaoke.to_json(fichero)
    karaoke.do_local()
    karaoke.to_json(fichero,'local.json')
    print('=============================')
    karaoke.__srt__()
    
