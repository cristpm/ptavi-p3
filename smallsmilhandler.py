#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar smil
    """

    def __init__(self):
        """
        Constructor. Inicializamos las variables
        """
        self.misdatos = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        dat_etiqueta = {}
        dat_atrib = {}
        root = ['width', 'height', 'background-color']
        reg = ['id', 'top', 'bottom', 'left', 'right']
        img = ['sre', 'region', 'begin', 'dur']
        aud = ['sre', 'begin', 'sur']
        text = ['sre', 'region']
        etiquetas = {'root-layout': root, 'region': reg, 'img': img,
         'audio': aud, 'textstream': text}
        if name in etiquetas:
            for atributo in etiquetas[name]:
                if attrs.get(atributo, "") != "":
                    dat_atrib[atributo] = attrs.get(atributo, "")
            dat_etiqueta[name] = dat_atrib
            self.misdatos.append(dat_etiqueta)

    def get_tags(self):
        return self.misdatos

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    misdatos = cHandler.get_tags()
    for e in misdatos:
        print("========================")
        print(e)
        print("========================")
