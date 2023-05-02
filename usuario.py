#!/usr/bin/python3

import json

class Usuario():
    def __init__(self, persistencia, nom=None, nick=None, password=None, id=None):
        self._nom = nom
        self._nick = nick
        self._password = password
        self._id = id
        self._persistencia = persistencia

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, valor):
        self._nom = valor

    @property
    def nick(self):
        return self._nick
    
    @nick.setter
    def nick(self, valor):
        self._nick = valor

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, valor):
        self._password = valor

    def desa(self):
        resultat = self._persistencia.desa(self)
        if resultat:
            self._id = resultat.id
        return resultat
    
    def llegeix_amb_nick(self):
        resultat = self._persistencia.llegeix_amb_nick(self._nick)
        return resultat

    def get_usuari_by_nick(self, nick):
        pass

    def get_usuari_by_api_key(self, key):
        pass

    def autentica(self, usuari, password):
        pass

    def __str__(self):
        resultat = {'id': self._id, 'nom': self.nom, 'nick': self._nick, 'password': self.password}
        return json.dumps(resultat)