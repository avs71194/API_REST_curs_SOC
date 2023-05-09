#!/usr/bin/python3

import json

class Pagaments():

    def __init__(self, total, pagat):
        self._total = total
        self._pagat = pagat
        self._canvi = None

    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self, valor):
        self._total = valor

    @property
    def pagat(self):
        return self._pagat
    
    @pagat.setter
    def pagat(self, valor):
        self._pagat = valor

    def canvi(self):
        self._canvi = self._pagat - self._total

    def __str__(self):
        return json.dumps({"Total": self._total, "Pagat": self._pagat, "Canvi": self._canvi})
