#!/usr/bin/python3

class App_tasques():
    def __init(self):
        self._llista = []

    def afeguir_tasca(self, tasca_nova):
        self._llista.append(tasca_nova)

    def lleguir_tasques(self):
        return self._llista