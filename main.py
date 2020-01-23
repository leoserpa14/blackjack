from random import shuffle

valores = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
           "K": 10, "A's": 11}

class Carta:
	def __init__(self, naipe, face):
		self.naipe = naipe
		self.face = face
		self.valor = valores[self.face]
		self.info = str(self.face + " de " + self.naipe)


class Baralho:
	def __init__(self):
		self.naipes = ["Copas", "Paus", "Ouro", "Espada"]
		self.faces = ["A's", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		self.cartas = []

	def create(self):
		for np in self.naipes:
			for fa in self.faces:
				self.cartas.append(Carta(naipe=np, face=fa))
		return self.cartas


class Jogador:
	def __init__(self):
		self.hand = []


class Mesa:
	def __init__(self, dealer, jogador, deck):
		self.dealer = dealer
		self.jogador = jogador
		self.deck = deck

	def hit(self, player):
		player.hand.append(self.deck[0])
		self.deck.pop(0)


baralho = Baralho().create()

deck = baralho * 6
shuffle(deck)

jogador = Jogador()
dealer = Jogador()

mesa = Mesa(dealer, jogador, deck)
mesa.hit(mesa.dealer)
mesa.hit(mesa.jogador)
mesa.hit(mesa.jogador)
mesa.hit(mesa.dealer)


print("Mão do Dealer: " + mesa.dealer.hand[0].info)
print("Sua mão: " + mesa.jogador.hand[0].info + " e " + mesa.jogador.hand[1].info)


mao_jogador = [mesa.jogador.hand[0].valor, mesa.jogador.hand[1].valor]
pontos = sum(mao_jogador)

if pontos == 21:
	print("Blackjack! Você ganhou!")
	exit()

while True:
	n = input("Quer mais uma carta? (S/N): ")

	if n == "S" or n == "s":
		# Pega uma carta
		mesa.hit(mesa.jogador)
		# Print as cartas que vc tem na mão
		a = len(mesa.jogador.hand)
		print("Sua mão: ")
		for i in range(a):
			print(mesa.jogador.hand[i].info + " (" + str(mesa.jogador.hand[i].valor) + ")")
		mao_jogador.append(mesa.jogador.hand[a-1].valor)

		# Soma a sua pontuação total
		pontos = sum(mao_jogador)
		print("Total: " + str(pontos))

		# Busted!
		if pontos > 21:
			print("Você perdeu!")
			break
		# Com 21 vc não vai querer mais cartas
		if pontos == 21:
			print("21!")
			break

	if n == "N" or n == "n":
		break

print("\nMão do Dealer: " + mesa.dealer.hand[0].info + " e " + mesa.dealer.hand[1].info)

mao_dealer = [mesa.dealer.hand[0].valor, mesa.dealer.hand[1].valor]

while True:
	pontos_dealer = sum(mao_dealer)
	if pontos_dealer < 16:
		mesa.hit(mesa.dealer)
		a = len(mesa.dealer.hand)
		print("Dealer recebeu " + mesa.dealer.hand[a-1].info)
		mao_dealer.append(mesa.dealer.hand[a-1].valor)
	elif 16 <= pontos_dealer < 21:
		break
	if pontos_dealer > 21:
		print("Dealer busted! Você ganhou!")
		exit()

print("\nResultado final\n ")
len_d = len(mesa.dealer.hand)
len_j = len(mesa.jogador.hand)

print("Mão do Dealer: " + str(pontos_dealer))
for i in range(len_d):
	print(mesa.dealer.hand[i].info)

print("\nSua mão: " + str(pontos))
for i in range(len_j):
	print(mesa.jogador.hand[i].info)


if pontos > pontos_dealer:
	print("\nJogador campeão!")

if pontos < pontos_dealer:
	print("\nVocê perdeu!")

if pontos == pontos_dealer:
	print("\nEmpate!")
