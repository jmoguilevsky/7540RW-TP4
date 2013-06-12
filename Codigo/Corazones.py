from Carta import Carta
from Mazo import Mazo

class JuegoCorazones(object):
	"""Clase que representa un juego de Corazones"""

	def __init__(self, jugadores):
		"""Crea un juego en base a 4 jugadores"""
		raise NotImplementedError

	def termino(self):
		"""Devuelve True si alguno de los jugadores alcanzo los 100 puntos"""
		raise NotImplementedError

	def imprimir_puntajes(self):
		"""Imprime los puntajes de cada jugador hasta el momento"""
		raise NotImplementedError

	def barajar(self):
		"""Crea un mazo nuevo, lo mezcla y le reparte una carta a cada jugador hasta
		que el mismo queda vacio."""
		raise NotImplementedError

	def identificar_jugador_que_inicia(self):
		"""Se fija cual de los 4 jugadores es primero y devuelve su id."""
		raise NotImplementedError

	def identificar_jugador_que_perdio(self, cartas_jugadas, id_primero):
		"""Recibe las 4 cartas jugadas en la mano y el id del jugador que abrio
		la jugada. Devuelve el id del jugador que perdio.
		Pierde el jugador que juega la carta mas alta del palo con el que inicio
		la jugada el primer jugador.
		Las cartas por orden creciente son: 2, 3,..., 10, J, Q, K, A."""
		raise NotImplementedError

	def procesar_e_informar_resultado(self, cartas_jugadas, id_primero, id_perdedor):
		"""Recibe las cartas de la jugada, el id del primer jugador, y el id del
		jugador que perdio.
		Almacena lo necesario para llevar la cuenta de puntos e informa a todos
		los jugadores del resultado de la jugada."""
		raise NotImplementedError

	def hay_corazones(self, cartas):
		"""Devuelve True si hay algun corazon entre las cartas pasadas"""
		raise NotImplementedError

	def realizar_jugada(self, nro_mano, nro_jugada, id_primero, corazon_jugado):
		"""Recibe el numero de mano, de jugada el id del primer jugador y si ya
		se jugaron corazones hasta el momento.
		Hace jugar una carta a cada uno de los jugadores empezando por el primero.
		Devuelve las 4 cartas jugadas."""
		raise NotImplementedError

	def calcular_puntajes(self):
		"""Al finalizar la mano, calcula y actualiza los puntajes de los jugadores.
		Cada jugador suma un punto por cada corazon levantado en la mano y 13 puntos
		si levanto la Q de picas, salvo en el caso de que un solo jugador haya
		levantado todos los corazones y la Q de picas, caso en el cual todos los
		jugadores salvo el suman 26 puntos."""
		raise NotImplementedError

	def intercambiar_cartas(self, nro_mano):
		"""Antes de hacer la primer jugada se pasan 3 cartas entre los rivales.
		En la primer mano, las cartas se pasan al jugador de la izquierda; en la
		segunda al jugador de la derecha; en la tercera al jugador del frente y
		en la cuarta no se pasan cartas. A partir de la quinta mano, se repite el
		mismo ciclo.
		El metodo debe primero pedirle las 3 cartas a pasar a cada oponente y luego
		entregarle las cartas que le fueron pasadas."""
		raise NotImplementedError

	def ganadores(self):
		"""Una vez terminado el juego, devuelve la lista de ganadores.
		Son ganadores todos los jugadores que hayan alcanzado el menor puntaje."""
		raise NotImplementedError

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
		"""Juega una partida completa de Corazones."""
		nro_mano = 1
		while not self.termino():
			print "Mano %d" % nro_mano
			self.barajar()
			self.intercambiar_cartas(nro_mano)
			self.jugar_mano(nro_mano)
			self.calcular_puntajes()
			self.imprimir_puntajes()

			nro_mano += 1
