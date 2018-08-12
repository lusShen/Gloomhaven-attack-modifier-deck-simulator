import random
import sys

from itertools import chain


orig_stdout = sys.stdout
test_number = 1000000
attack_per_turn = 1
base_damage = 1

class Ability(dict):
	def __missing__(self, key):
		return 0


class Attack_modifier_card:
	def __init__(self, name='' ,modifier = 0 , condition = set(), ability = Ability() , roll = False, shuffle_marker = False, loss = False):
		self.name = name
		self.modifier = modifier 
		self.condition = condition #include wound, poison ... etc
		self.ability = ability #include bless x, curse x, pierce x, push x ...etc, any ability with a number
		self.roll = roll 
		self.shuffle_marker = shuffle_marker #a card with shuffle_marker cause the shuffle
		self.loss = loss #a card with loss won't back to the deck once it's drawn
		
	def __gt__(self, that):
	
		#same condition & same otherAbility, then compare modifier
		if (self.condition == that.condition and self.ability == that.ability ):
			return (self.modifier > that.modifier)
		
		
		if (len(self.condition) + len(self.ability) ==0):
			if (self.modifier > that.modifier):
				return None
			else:
				return False
				
		if (len(that.condition) + len(that.ability) ==0):
			if (self.modifier > that.modifier):
				return True
			else:
				return None

		return None


	def __add__(self, other):#add 2 card = the result of the rolling stack, treat as a card
		temp = Attack_modifier_card(
			modifier = self.modifier + other.modifier,
			condition = self.condition.union(other.condition),
			)

		temp.ability = Ability(dict())
		for k,v in chain(self.ability.items(), other.ability.items()):
			temp.ability[k] += v
		
		if (self.roll and other.roll):
			temp.roll = True
		else:
			temp.roll = False
		
		#the main reason I name the result "card" knowing there is 2x/null in this rolling stack
		temp.name = self.name
		if (other.name is '2x' or other.name is 'null'):
			temp.name = other.name
		
		return temp


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

#basic cards
card_critical = Attack_modifier_card(name = '2x', shuffle_marker = True)
card_miss = Attack_modifier_card(name = 'null',modifier = -999, shuffle_marker = True)
card_0 = Attack_modifier_card(name = '0')
card_p1 = Attack_modifier_card(name = '+1',modifier = 1)
card_p2 = Attack_modifier_card(name = '+2',modifier = 2)
card_p4 = Attack_modifier_card(name = '+4',modifier = 4)
card_n1 = Attack_modifier_card(name = '-1',modifier = -1)
card_n2 = Attack_modifier_card(name = '-2',modifier = -2)


card_rollp1 = Attack_modifier_card(name = 'roll +1',modifier = 1 , roll=True)


card_p1immobilize = Attack_modifier_card(name = '+1 immobilize',modifier = 1 , condition = set(['immobilize']))
card_p1disarmd = Attack_modifier_card(name = '+1 disarmd',modifier = 1 , condition = set(['disarmd']))
card_p2wound = Attack_modifier_card(name = '+2 wound',modifier = 2 , condition = set(['wound']))
card_p2poison = Attack_modifier_card(name = '+2 poison',modifier = 2 , condition = set(['poison']))
card_p2curse = Attack_modifier_card(name = '+2 curse',modifier = 2 , ability = Ability([('curse',1)]))
card_p3muddle = Attack_modifier_card(name = '+3 muddle',modifier = 3 , condition = set(['muddle']))
card_stun = Attack_modifier_card(name = '+0 stun',modifier = 0 , condition = set(['stun']))


card_rollcurse  = Attack_modifier_card(name = 'roll curse',modifier = 0 , roll=True , ability = Ability([('curse',1)]) )


deck = [
	card_critical,
	card_miss,
	
	#card_0,
	#card_0,
	#card_0,
	#card_0,
	#card_0,
	#card_0,
	#card_n2,
	#card_n1,
	#card_n1,
	#card_n1,
	#card_n1,
	#card_n1,

	card_p2,
	card_p1,
	#card_p1,
	#card_p1,
	#card_p1,
	#card_p1,
	
	
	#Scoundrel
	#card_0,
	#card_p2,
	#card_p2,
	#card_p1,
	#card_rollp1,
	#card_rollp1,
	#card_rollp1,
	#card_rollp1,
	#card_rollpierce3,
	#card_rollpierce3,
	#card_rollpoison,
	#card_rollpoison,
	#card_rollpoison,
	#card_rollpoison,
	#card_rollmuddle,
	#card_rollmuddle,
	#card_rollinvisible
	
	
	#3 arrow
	#card_rollp1,
	#card_rollp1,
	#card_rollp1,
	#card_rollp1,
	#card_p2,
	#card_p2,
	#card_p1,
	#card_p1,
	#card_rollmuddle,
	#card_rollmuddle,
	#card_rollmuddle,
	#card_rollpierce3,
	#card_rollpierce3,
	#card_rollstun,
	#card_rolladdtarger,
	#card_item,
	#card_item,
	#card_item

	#music note
	card_p1immobilize,
	card_p1disarmd,
	card_p2wound,
	card_p2poison,
	card_p2curse,
	card_p3muddle,
	card_stun,
	
	card_rollcurse,
	card_rollcurse,
	card_rollcurse,
	card_rollcurse,
	
	card_p4,
	card_p4,
	card_rollp1,
	card_rollp1,
	#card_rollp1
]


def Deck_simulation(deck,filename, base_damage = 2,test_number = 1000000, adv = 0,attack_per_turn = 1):
	Deck = AMC_deck(cards = deck)
	Deck.shuffle_deck()
	f = open(filename, "w")
	sys.stdout = f
	print ("damage\tcondition\tability")
	j=0
	for i in range(test_number):
		j=j+1
		
		if (adv==0):
			card = Deck.draw()
		elif(adv ==-1):
			card = Deck.draw2(base_damage = base_damage , adv= False)
		elif(adv ==1):
			card = Deck.draw2(base_damage = base_damage , adv= True)
		
		damage = 0
		if (card.name is '2x'):
			damage = (base_damage+ card.modifier)* 2
		elif (card.name is'null'):
			damage = 0
		else:
			damage = base_damage + card.modifier
		if (damage <0):
			damage = 0
		#print (damege ,"\t" ,card.condition)
		if (len(card.condition) >0):
			condition = card.condition
		else:
			condition = ""
		if (len(card.ability) >0):
			ability = card.ability
		else:
			ability = "";
		print ("%d\t%s\t%s" % (damage,condition,ability))
		if (j == attack_per_turn):
			Deck.turn_end()
			j=0


	sys.stdout = orig_stdout
	f.close()

Deck_simulation(deck,base_damage = base_damage,  test_number = test_number , adv = 0 , attack_per_turn = attack_per_turn , filename = 'normal.txt')
print ("normal finish!")
Deck_simulation(deck,base_damage = base_damage,test_number = test_number , adv = 1 , attack_per_turn = attack_per_turn , filename = 'adv.txt')
print ("advantage finish!")
Deck_simulation(deck,base_damage = base_damage,test_number = test_number , adv = -1 , attack_per_turn = attack_per_turn , filename = 'disadv.txt')
print ("disadvantage finish!")