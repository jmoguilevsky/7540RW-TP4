from random import shuffle
from Carta import Carta

class Mazo(object):
    """Representa a un mazo de barajas inglesas"""
    def __init__(self):
        """Inicializa un mazo con sus 52 cartas"""
        self.cartas = []

        for numero in xrange(1, 13 + 1):
            for palo in (Carta.CORAZONES, Carta.DIAMANTES, Carta.PICAS, Carta.TREBOLES):
                self.cartas.append(Carta(numero, palo))

    def mezclar(self):
        """Mezcla el mazo"""
        shuffle(self.cartas)

    def obtener_tope(self):
        """Quita la carta que esta encima del mazo y la devuelve"""
        return self.cartas.pop()

    def es_vacio(self):
        """Devuelve True si al mazo no le quedan cartas, False caso contrario"""
        return len(self.cartas) == 0
