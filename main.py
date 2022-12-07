# Jonah Warshawsky. groupe 401
# Les exercises de programmation orientée objet

from math import pi
from random import randint

class StringFoo:
    def __init__(self):
        self.string = ""

    def set_string(self, string):
        self.string = string

    def print_string(self):
        print(self.string.upper())


class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calcul_aire(self):
        return self.largeur * self.hauteur

    def print_infos(self):
        print(f"Largeur: {self.largeur}, Hauteur: {self.hauteur}, Aire: {self.calcul_aire()}")

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        return pi * self.rayon ** 2

    def calcul_circonference(self):
        return 2 * pi * self.rayon


class Hero:
    def __init__(self, nom):
        self.nom = nom
        self.vie = randint(1, 10) + randint(1, 10)
        self.force_attaque = randint(1, 6)
        self.force_defense = randint(1, 6)

    def attaquer(self):
        return randint(1, 6) + self.force_attaque

    def recevoir_degats(self, degats):
        self.vie -= degats - self.force_defense

    def est_vivant(self):
        return self.vie > 0



