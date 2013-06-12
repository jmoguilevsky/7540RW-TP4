from Carta import Carta
from Mazo import Mazo

class JuegoCorazones(object):
    """ Clase que representa un juego de Corazones.

    Atributos:
        jugadores: lista de jugadores.
        jugadores_id: lista con los id de los jugadores.
        puntajes: lista con los puntajes de los jugadores.
        mazo: instancia de Mazo con el que se juega.
        turno: entero representando el índice del jugador al que le toca
        jugar primero en el próximo turno.
    """

    def __init__(self, jugadores):
        """ Crea un juego en base a una lista de jugadores.

        Argumentos:
            jugadores: lista con instancias de Jugador.

        Excepciones:
            ValueError: hay más del límite de jugadores.
        """

        if len(jugadores) != 4:
            raise ValueError("No pueden haber más de 4 jugadores.")

        self.jugadores = jugadores
        self.jugadores_id = [jugador.obtener_id_jugador() for jugador in self.jugadores]
        self.puntajes = [0, 0, 0, 0]
        self.mazo = None
        self.turno = -1
        self.cartas_levantadas = {}

        for id in self.jugadores_id:
            self.cartas_levantadas[id] = []

    def termino(self):
        """ Devuelve True si alguno de los jugadores alcanzo los 100 puntos. """

        for puntaje in self.puntajes:
            if puntaje >= 100:
                return True

        return False

    def imprimir_puntajes(self):
        """ Imprime los puntajes de cada jugador hasta el momento. """

        for n in xrange(len(self.jugadores)):
            print self.jugadores[n], self.puntajes[n]

    def barajar(self):
        """ Crea un mazo nuevo, lo mezcla y le reparte una carta a cada jugador hasta
        que el mismo queda vacío. """

        self.mazo = Mazo()
        self.mazo.mezclar()

        while not self.mazo.es_vacio():
            for n in xrange(len(self.jugadores)):
                self.jugadores[n].recibir_carta(self.mazo.obtener_tope())

        self.turno = -1

    def identificar_jugador_que_inicia(self):
        """ Se fija cual de los jugadores es primero y devuelve su id. """

        if self.turno == -1:
            # Estamos en el primer turno. Buscar el jugador que tiene el 2
            # de treboles.

            self.turno = 0

            for jugador in jugadores:
                if jugador.es_primero():
                    break

                self.turno += 1

        return self.jugadores_id[self.turno]

    def identificar_jugador_que_perdio(self, cartas_jugadas, id_primero):
        """ Recibe las cartas jugadas en la mano y el id del jugador que
        abrió la jugada. Devuelve el id del jugador que perdió.

        Pierde el jugador que juega la carta mas alta del palo con el que
        inicio la jugada el primer jugador. Las cartas por orden creciente
        son: 2, 3,..., 10, J, Q, K, A. """

        # Definimos cuál es la carta más alta.
        indice_carta = 0

        for indice in xrange(1, len(cartas_jugadas)):
            if cartas_jugadas[indice].obtener_palo() == cartas_jugadas[0].obtener_palo():
                numero = cartas_jugadas[indice].obtener_numero()

                if numero == 1:
                    # La carta es el As, así que dejamos de recorrer.
                    indice_carta = indice
                    break
                elif cartas_jugadas[indice_carta].obtener_numero == 1:
                    # La carta de indice máximo ya es el As.
                    break
                elif numero > cartas_jugadas[indice_carta].obtener_numero():
                    indice_carta = indice

        # Indice del jugador que tiró la carta más alta.
        try:
            indice_jugador = jugadores_id.index(id_primero) + indice_carta
        except ValueError:
            raise ValueError("El primer jugador no existe.")

        # Hacemos que el indice del jugador quede determinado.
        while not 0 <= indice_jugador < len(self.jugadores):
            indice_jugador -= len(self.jugadores)

        return self.jugadores_id[indice_jugador]

    def __contar_puntos_en_lista(self, cartas):
        """ Cuenta el puntaje que obtiene el jugador que levantó las cartas
        en la lista. """

        puntos = 0

        for carta in cartas:
            if carta.obtener_palo() == Carta.CORAZONES:
                puntos += 1
            elif carta.obtener_palo() == Carta.PICAS and carta.obtener_numero == Carta.NUMEROS.index("Q"):
                puntos += 13

        return puntos

    def procesar_e_informar_resultado(self, cartas_jugadas, id_primero, id_perdedor):
        """ Recibe las cartas de la jugada, el id del primer jugador, y el id del
        jugador que perdió.

        Almacena lo necesario para llevar la cuenta de puntos e informa a todos
        los jugadores del resultado de la jugada. """

        ## TODO: TERMINAR ################################################
        try:
            self.turno = jugadores_id.index(id_perdedor)
        except ValueError:
            raise ValueError("El no existe el jugador perdedor.")

        self.cartas_levantadas[id_perdedor].append(cartas_jugadas)

        puntos_luna = self.__contar_puntos_en_lista(self.cartas_levantadas[id_perdedor])

        if puntos_luna == 26:
            self.puntajes[self.turno] -= 26
            pass

        puntos_jugada = self.__contar_puntos_en_lista(cartas_jugadas)

        for jugador in self.jugadores:
            jugador.conocer_jugada(cartas_jugadas, id_primero, id_perdedor)

        raise NotImplementedError

    def hay_corazones(self, cartas):
        """ Devuelve True si hay algun corazon entre las cartas pasadas. """

        for carta in cartas:
            if carta.obtener_palo == Carta.CORAZONES:
                return True

        return False

    def realizar_jugada(self, nro_mano, nro_jugada, id_primero, corazon_jugado):
        """ Recibe el numero de mano, de jugada el id del primer jugador y si ya
        se jugaron corazones hasta el momento.

        Hace jugar una carta a cada uno de los jugadores empezando por el primero.
        Devuelve las 4 cartas jugadas. """
        raise NotImplementedError

    def calcular_puntajes(self):
        """Al finalizar la mano, calcula y actualiza los puntajes de los jugadores.
        Cada jugador suma un punto por cada corazon levantado en la mano y 13 puntos
        si levanto la Q de picas, salvo en el caso de que un solo jugador haya
        levantado todos los corazones y la Q de picas, caso en el cual todos los
        jugadores salvo el suman 26 puntos."""
        raise NotImplementedError

    def intercambiar_cartas(self, nro_mano):
        """ Antes de hacer la primer jugada se pasan 3 cartas entre los rivales.

        En la primer mano, las cartas se pasan al jugador de la izquierda; en la
        segunda al jugador de la derecha; en la tercera al jugador del frente y
        en la cuarta no se pasan cartas. A partir de la quinta mano, se repite el
        mismo ciclo.

        El metodo debe primero pedirle las 3 cartas a pasar a cada oponente y luego
        entregarle las cartas que le fueron pasadas. """
        raise NotImplementedError

    def ganadores(self):
        """ Una vez terminado el juego, devuelve la lista de ganadores.

        Son ganadores todos los jugadores que hayan alcanzado el menor
        puntaje. """

        ganadores = []

        for indice, jugador in enumerate(self.jugadores):

            if min(self.puntajes) == self.puntajes[indice]:
                ganadores.append(jugador)

        return ganadores

    def jugar_mano(self, nro_mano):
        """Realiza las 13 jugadas que corresponden a una mano completa."""
        corazon_jugado = False
        id_primero = self.identificar_jugador_que_inicia()

        # INICIO: Chequeos de trampa
        palos_faltantes = [[], [], [], []]
        cartas_en_mesa = []
        solo_tiene_corazones = [False] * 4
        # FIN: Chequeos de trampa

        for nro_jugada in xrange(1, 13 + 1):
            print "Jugada %i" % nro_jugada
            print "Empieza %s" % self.jugadores[id_primero]

            cartas_jugadas = self.realizar_jugada(nro_mano, nro_jugada, id_primero, corazon_jugado)

            id_perdedor = self.identificar_jugador_que_perdio(cartas_jugadas, id_primero)
            print "Levanta %s" % self.jugadores[id_perdedor]

            self.procesar_e_informar_resultado(cartas_jugadas, id_primero, id_perdedor)


            # INICIO: Chequeos de trampa
            if nro_jugada == 1 and not cartas_jugadas[0] == Carta(2, Carta.TREBOLES):
                raise Exception("El primer jugador no jugo el 2 de treboles""")
            if nro_jugada == 1 and (corazon_jugado or Carta(12, Carta.PICAS) in cartas_jugadas):
                raise Exception("Jugador jugo carta especial en primer juego""")
            for i in xrange(4):
                if cartas_jugadas[i].obtener_palo() in palos_faltantes[(i + id_primero) % 4]:
                    raise Exception("El jugador %s dijo que no tenia %s" % (self.jugadores[(i + id_primero) % 4], Carta.PALOS[cartas_jugadas[i].obtener_palo()]))
                if solo_tiene_corazones[(i + id_primero) % 4] and cartas_jugadas[i].obtener_palo() != Carta.CORAZONES:
                    raise Exception("El jugador %s dijo que solo tenia %s" % (self.jugadores[(i + id_primero) % 4], Carta.PALOS[Carta.CORAZONES]))
            palo_jugada = cartas_jugadas[0].obtener_palo()
            for i in xrange(1, 4):
                if cartas_jugadas[i].obtener_palo() != palo_jugada and palo_jugada not in palos_faltantes[(i + id_primero) % 4]:
                    palos_faltantes[(i + id_primero) % 4].append(palo_jugada)
            for carta in cartas_jugadas:
                if carta in cartas_en_mesa:
                    raise Exception("Alguien se matufio el %s" % carta)
                cartas_en_mesa.append(carta)
            if not corazon_jugado and palo_jugada == Carta.CORAZONES:
                solo_tiene_corazones[id_primero] = True
            # FIN: Chequeos de trampa


            corazon_jugado = corazon_jugado or self.hay_corazones(cartas_jugadas)

            id_primero = id_perdedor

    def jugar(self):
        """ Juega una partida completa de Corazones. """
        nro_mano = 1

        while not self.termino():
            print "Mano %d" % nro_mano
            self.barajar()
            self.intercambiar_cartas(nro_mano)
            self.jugar_mano(nro_mano)
            self.calcular_puntajes()
            self.imprimir_puntajes()

            nro_mano += 1
