class Carta(object):
    """Representa a una carta de la baraja inglesa"""

    # Constantes para los palos
    CORAZONES = 0
    DIAMANTES = 1
    PICAS = 2
    TREBOLES = 3

    # Diccionarios para la impresion:
    NUMEROS = ["A"] + [str(n) for n in xrange(2, 11)] + ["J", "Q", "K"]
    PALOS = ['corazones', 'diamantes', 'picas', 'treboles']

    def __init__(self, numero, palo):
        """Crea una carta desde su numero y su palo"""
        if not 1 <= numero <= 13 or not 0 <= palo <= 3:
            raise ValueError

        self.palo = palo
        self.numero = numero

    def obtener_palo(self):
        return self.palo

    def obtener_numero(self):
        return self.numero

    def __eq__(self, otro):
        return self.palo == otro.palo and self.numero == otro.numero

    def __str__(self):
        return "%s de %s" % (Carta.NUMEROS[self.numero - 1], Carta.PALOS[self.palo])

