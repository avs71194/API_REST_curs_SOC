#!/usr/bin/python3
import json

class Radar():

    def __init__(self,velocidad_coche, velocidad_via):
        self._velocidad_coche = velocidad_coche
        self._velocidad_via = velocidad_via

    @property
    def velocidad_coche(self):
        return self._velocidad_coche
    
    @velocidad_coche.setter
    def velocidad(self, valor):
        self._velocidad_coche = valor

    @property
    def velocidad_via(self):
        return self._velocidad_via
    
    @velocidad_via.setter
    def velocidad_via(self, valor):
        self._velocidad_via = valor

    def calculo_velocidad(self):
        if self._velocidad_coche <= self._velocidad_via:
            return json.dumps({"Resultat": "Correcte"})
        elif self._velocidad_coche < self._velocidad_via * 1.1:
            return json.dumps({"Resultat": "Marge de Seguretat"})
        else:
            return json.dumps({"Resultat": "Multa"})