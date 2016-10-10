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


class KaraokeLocal():

    def __init__(self, fichero):
        parser = make_parser()
        self.cHandler = SmallSMILHandler()
        parser.setContentHandler(self.cHandler)
        parser.parse(open(fichero))
        self.misdatos = self.cHandler.get_tags()

    def __srt__(self):
        for tags in self.misdatos:
            for etiqueta, atributos in tags.items():
                linea = etiqueta + "\t"
                for c, v in atributos.items():
                    linea = linea + c + "=" + "\"" + v + "\"" + "\t"
                print(linea)

    def to_json(self, fichero, f_json = fichero[:-4] + "json"):
        json.dump(self.misdatos, open(f_json, 'w'))

    def do_local(self):
        for tags in self.misdatos:
            for etiqueta, atributos in tags.items():
                if 'src' in atributos:
                    remoto = atributos['src']
                    if remoto[:4] == 'http':
                        local = remoto.split('/')[-1]
                        urllib.request.urlretrieve(remoto, local)
                        atributos['src'] = local


if __name__ == "__main__":
    """
    Programa principal
    """
    karaoke = KaraokeLocal(fichero)
    karaoke.__srt__()
    karaoke.to_json(fichero)
    karaoke.do_local()
    karaoke.to_json(fichero, 'local.json')
    karaoke.__srt__()
