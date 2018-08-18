
from object.GH_AMC_deck import AMC_deck
from data.card.common_card import Basic_card
from data.deck.basic_deck import Basic_deck
import copy

#default perks = Brute_perk
from data.deck.base_character import basic_class


#for specific class, so the deck include the perks


class AMC_class_deck(AMC_deck):
	def __init__(self, perks = basic_class['Brute'],deck = Basic_deck):
		super(AMC_class_deck,self).__init__(cards = deck.deck)
		self.perks = copy.deepcopy(perks)
		
	def check_perk(self, name):
		if not(name in self.perks):
			#error: no perk have this name
			return
		if (self.perks[name]['available']>0):
			self.perks[name]['available']-=1
			for s in (self.perks[name]['modification']) :
				card, action , count = s
				if (action == 'a'):
					for _ in range(count):
						self.add_card(card)
				elif (action == 'r'):
					for _ in range(count):
						self.remove_card(card)
		else:
			#error: no available
			return

	def redo_check_perk(self, name):
		#to do: add limitation that available won't get over the initial number
		if not(name in self.perks):
			#error: no perk have this name
			return
		self.perks[name]['available']+=1
		for set in self.perks[name]['modification'] :
			card, action , count = set
			if (action == 'r'):
				for _ in range(count):
					self.add_card(card)
			elif (action == 'a'):
				for _ in range(count):
					self.remove_card(card)
					
	def check_all(self):
		for k,p in self.perks.items():
			for i in range(p['available']):
				self.check_perk(k)


