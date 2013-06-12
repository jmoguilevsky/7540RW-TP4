from Carta import Carta

class Jugador(object):
    """Clase que representa a un jugador de Corazones"""

    def __init__(self, id_jugador, nombre):
        """Crea el jugador desde su id y su nombre. El id es un numero en el rango 0..3"""
        self.id_jugador = id_jugador
        self.nombre = nombre
        self.mano = []

    def obtener_id_jugador(self):
        """Devuelve el id del jugador"""
        return self.id_jugador

    def recibir_carta(self, carta):
        """Recibe una carta y la agrega a su mano"""
        self.mano.append(carta)

    def es_primero(self):
        """Devuelve True si el usuario tiene el 2 de treboles"""
        return Carta(2, Carta.TREBOLES) in self.mano

    def devolver_cartas_a_pasar(self, id_jugador):
        """Antes de comenzar la mano, retira de su mano y devuelve 3 cartas para
        pasarle al oponente con id id_jugador"""
        raise NotImplementedError

    def recibir_cartas_pasadas(self, id_jugador, cartas):
        """Antes de comenzar la mano y despues de haber devuelto sus cartas, recibe
        3 cartas del oponente con id id_jugador"""
        self.mano += cartas

    def jugar_carta(self, nro_mano, nro_jugada, cartas_jugadas, corazon_jugado):
        """Saca una carta de su mano y la devuelve jugandola. Recibe el numero de
        mano, el numero de jugada, las cartas ya jugadas en la mesa en esa jugada
        y un booleano que indica si ya se jugaron corazones en las jugadas previas.
        Si ya hay cartas_jugadas y el jugador posee una carta del palo de la primer
        carta debe jugarla obligatoriamente.
        Si nro_jugada es 1 y no hay cartas_jugadas, el jugador debe jugar el 2 de
        treboles.
        Si nro_jugada es 1 el jugador no puede jugar ni un corazon ni la Q de picas.
        Si no hay cartas_jugadas y corazon_jugado es False el jugador no podra jugar
        un corazon salvo que no tenga otra carta."""
        raise NotImplementedError

    def conocer_jugada(self, cartas_jugadas, id_primer_jugador, id_jugador_que_levanto):
        """Luego de terminada la jugada, se informa al jugador sobre las cartas que
        se jugaron, en que orden y cual fue el id del jugador que levanto las cartas
        del juego."""
        pass

    def __str__(self):
        """Representacion del jugador"""
        return "%s (%d)" % (self.nombre, self.id_jugador)
