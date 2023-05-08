#!/usr/bin/python3
import json

class Gosso():

    def __init__(self, edad_perro):
        self._edad_perro = edad_perro
        self._equivalencia = None

    @property
    def edad_perro(self):
        return self._edad_perro
    
    @edad_perro.setter
    def edad_perro(self, valor):
        self._edad_perro = valor

    def calculo_edad(self):
        if self._edad_perro <=2:
            self._equivalencia  = self._edad_perro * 10.5
        else:
            self._equivalencia = 21 + (self._edad_perro-2) * 4

    def __str__(self):
        return json.dumps({"edat_del_gos": self._edad_perro, "equivalencia_humana": self._equivalencia})