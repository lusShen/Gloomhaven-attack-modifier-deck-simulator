import random
from GH_AMC import Ability, Attack_modifier_card

class AMC_deck:
	def __init__(self, cards = [] ):
		self.deck = cards
		self.shuffle_marker = False
		self.discard = []
		
	def add_card(self, card):
		#add a card and shuffle
		self.deck.append(card)
		random.shuffle(self.deck)
		
	def shuffle_deck(self):
		self.deck.extend(self.discard)
		self.discard.clear()
		random.shuffle(self.deck)
		
	
	def turn_end(self):
		if (self.shuffle_marker):
			self.shuffle_deck()
			self.shuffle_marker = False
	
	def __check_deck(self):
		if (len(self.deck) == 0):
			self.shuffle_deck()
		
	
	def draw(self):
		self.__check_deck()
		card = self.deck.pop()
		cardInPlay = []
		
		if (card.loss == False):
			cardInPlay.append(card)
			
		if (card.shuffle_marker):
			self.shuffle_marker = True

		while (card.roll):
			self.__check_deck()
			new_card = self.deck.pop()
			card = card + new_card
			if (new_card.loss == False):
				cardInPlay.append(new_card)
		
		self.discard.extend(cardInPlay)
		
		return card
		
	def draw2(self, adv = True, base_damage = 2):
		self.__check_deck()
		card1 = self.deck.pop()
		self.__check_deck()
		card2 = self.deck.pop()
		cardInPlay = []
		result = card1
		
		
		if (card1.roll):
			result = card2 #default result of disadvantage
			
			temp = card1 + card2
			while(temp.roll):# both cards are roll
				self.__check_deck()
				card = self.deck.pop()
				if (card.roll == False and adv == False):
					result = card
				temp = temp + card
				if (card.loss == False):
					cardInPlay.append(card)
			if (adv):
				result =temp
		
		else:  # if (card1.roll == False)
			if (card2.roll):
				result = (card1 + card2) if adv else card1
			else: #in the case both cards not roll
				if card1.name is '2x':
					card1.modifier = base_damage 
				if card2.name is '2x':
					card2.modifier = base_damage 
				#change the modifier, help compare these cards
				if (card1 > card2 == None):
					result = card1
				elif (card1 > card2):
					result = card1  if adv else card2
				else:
					result = card2  if adv else card1
				
				if card1.name is '2x':
					card1.modifier = 0 
				if card2.name is '2x':
					card2.modifier = 0
		
		if (card1.shuffle_marker or card2.shuffle_marker):
			self.shuffle_marker = True

		if (card1.loss == False):
			self.discard.append(card1)
		if (card2.loss == False):
			self.discard.append(card2)
		
		self.discard.extend(cardInPlay)
		return result
