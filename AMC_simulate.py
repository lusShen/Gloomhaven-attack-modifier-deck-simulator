import random
import sys
orig_stdout = sys.stdout
test_number = 1000000
attack_per_turn = 1
base = 1

class attack_modifier_card:
	def __init__(self, name='' ,modifier = 0 , pierce = 0 , push = 0 , pull = 0, condition = '' , roll = False):
		self.name = name
		self.modifier = modifier
		self.pierce = pierce
		self.push = push
		self.pull = pull
		self.condition = condition
		self.roll = roll
		
	def __gt__(self, that):
		if (self.condition != that.condition and self.condition != '' and that.condition != ''):
			return None
		if (self.condition != ''):
			return True if (self.modifier >= that.modifier) else None
		if (that.condition != ''):
			return False if (that.modifier >= self.modifier) else None
		return (self.modifier > that.modifier)

	def __add__(self, other):#2 card will treat as 1 non-roll card
		temp = attack_modifier_card()
		temp.modifier = self.modifier + other.modifier
		temp.pierce = self.pierce + other.pierce
		temp.push = self.push + other.push
		temp.pull = self.pull + other.pull
		
		if len(self.condition) != 0:
			if len(other.condition) != 0:
				temp.condition = ",".join((self.condition , other.condition))
			else:
				temp.condition = self.condition
		else:
			temp.condition = other.condition
		
		if (self.roll and other.roll):
			temp.roll = True
		else:
			temp.roll = False
		temp.name = self.name
		if (other.name is '2x' or other.name is 'null'):
			temp.name = other.name
		
		return temp
		
		
class AMC_deck:
	shuffle_marker = False
	discard = []

	
	def __init__(self, cards = [] ):
		self.deck = cards
		
	def add_card(self, card):
		self.deck.append(card)
		
	def shuffle_deck(self):
		self.deck.extend(self.discard)
		self.discard.clear()
		random.shuffle(self.deck)
		
	
	def turn_end(self):
		if (self.shuffle_marker == True):
			self.shuffle_deck()
			self.shuffle_marker = False
	
	def __check_deck(self):
		if (len(self.deck) == 0):
			self.shuffle_deck()
		
	
	def draw(self):
		self.__check_deck()
		card = self.deck.pop()
		temp = []
		if (card.name != 'bless' or card.name != 'curse'):
			temp.append(card)
		if (card.name is '2x' or card.name is 'null'):
			self.shuffle_marker = True
		while (card.roll):
			self.__check_deck()
			new_card = self.deck.pop()
			card = card + new_card
			if (card.name != 'bless' or card.name != 'curse'):
				temp.append(new_card)
		
		self.discard.extend(temp)
		return card
		
	def draw2(self, adv = True, base = 2):
		self.__check_deck()
		card1 = self.deck.pop()
		self.__check_deck()
		card2 = self.deck.pop()
		c = []
		result = card1
		
		
		if (card1.roll):
			#if (adv == False):
			result = card2
			
			temp = card1 + card2
			while(temp.roll):
				self.__check_deck()
				card = self.deck.pop()
				if (card.roll == False and adv == False):
					result = card
				temp = temp + card
				if (card.name != 'bless' or card.name != 'curse'):
					c.append(card)
			if (adv):
				result =temp
		
		if (card1.roll == False):
			if (card2.roll):
				result = (card1 + card2) if adv else card1
			else: #in the case both cards not roll
				if card1.name is '2x':
					card1.modifier = base 
				if card2.name is '2x':
					card2.modifier = base 
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
		
		if (card1.name is '2x' or card1.name is 'null'):
			self.shuffle_marker = True
		if (card2.name is '2x' or card2.name is 'null'):
			self.shuffle_marker = True

		if (card1.name != 'bless' or card1.name != 'curse'):
			self.discard.append(card1)
		if (card2.name != 'bless' or card2.name != 'curse'):
			self.discard.append(card2)
		
		self.discard.extend(c)
		return result


card_critical = attack_modifier_card(name = '2x')
card_miss = attack_modifier_card(name = 'null',modifier = -999)
card_0 = attack_modifier_card(name = '0')
card_p1 = attack_modifier_card(name = '+1',modifier = 1)
card_p2 = attack_modifier_card(name = '+2',modifier = 2)
card_p4 = attack_modifier_card(name = '+4',modifier = 4)
card_n1 = attack_modifier_card(name = '-1',modifier = -1)
card_n2 = attack_modifier_card(name = '-2',modifier = -2)
card_rollp1 = attack_modifier_card(name = 'roll +1',modifier = 1 , roll=True)

card_p1immobilize = attack_modifier_card(name = '+1 immobilize',modifier = 1 , condition = 'immobilize')
card_p1disarmd = attack_modifier_card(name = '+1 disarmd',modifier = 1 , condition = 'disarmd')
card_p2wound = attack_modifier_card(name = '+2 wound',modifier = 2 , condition = 'wound')
card_p2poison = attack_modifier_card(name = '+2 poison',modifier = 2 , condition = 'poison')
card_p2curse = attack_modifier_card(name = '+2 curse',modifier = 2 , condition = 'curse')
card_p3muddle = attack_modifier_card(name = '+3 muddle',modifier = 3 , condition = 'muddle')
card_stun = attack_modifier_card(name = '+0 stun',modifier = 0 , condition = 'stun')
card_rollpoison  = attack_modifier_card(name = 'roll poison',modifier = 0 , roll=True , condition = 'poison')
card_rollcurse  = attack_modifier_card(name = 'roll curse',modifier = 0 , roll=True , condition = 'curse')
card_rollmuddle  = attack_modifier_card(name = 'roll muddle',modifier = 0 , roll=True , condition = 'muddle')
card_rollpierce3  = attack_modifier_card(name = 'roll muddle',modifier = 0 ,pierce = 3, roll=True )
card_rollstun  = attack_modifier_card(name = 'roll stun',modifier = 0 , roll=True , condition = 'stun')
card_rolladdtarger  = attack_modifier_card(name = 'addtarger',modifier = 0 , roll=True , condition = 'add targer')
card_item = attack_modifier_card(name = '+0 item',modifier = 0 , condition = 'item')
card_rollinvisible  = attack_modifier_card(name = 'roll invisible',modifier = 0 , roll=True , condition = 'invisible')

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
	
	card_p4,
	card_p4,
	card_rollp1,
	card_rollp1,
	#card_rollp1
]

Deck = AMC_deck(cards = deck)
Deck.shuffle_deck()
f = open("normal.txt", "w")
sys.stdout = f
print ("damage\tcondition\tpierce")
j=0
for i in range(test_number):
	j=j+1
	card = Deck.draw()
	#card = Deck.draw2(base = base , adv= False)
	#card = Deck.draw2(base = base , adv= True)
	damage = 0
	if (card.name is '2x'):
		damage = (base+ card.modifier)* 2
	elif (card.name is'null'):
		damage = 0
	else:
		damage = base + card.modifier
	if (damage <0):
		damage = 0
	#print (damege ,"\t" ,card.condition)
	print ("%d\t%s\t%d" % (damage,card.condition,card.pierce))
	if (j == attack_per_turn):
		Deck.turn_end()
		j=0


sys.stdout = orig_stdout
f.close()
print ("normal finish!")



Deck = AMC_deck(cards = deck)
Deck.shuffle_deck()
f = open("adv.txt", "w")
sys.stdout = f
print ("damage\tcondition\tpierce")
j=0
for i in range(test_number):
	j=j+1
	#card = Deck.draw()
	#card = Deck.draw2(base = base , adv= False)
	card = Deck.draw2(base = base , adv= True)
	damage = 0
	if (card.name is '2x'):
		damage = (base+ card.modifier)* 2
	elif (card.name is'null'):
		damage = 0
	else:
		damage = base + card.modifier
	if (damage <0):
		damage = 0
	#print (damege ,"\t" ,card.condition)
	print ("%d\t%s\t%d" % (damage,card.condition,card.pierce))
	if ( j == attack_per_turn):
		Deck.turn_end()
		j=0


sys.stdout = orig_stdout
f.close()
print ("advantage finish!")


Deck = AMC_deck(cards = deck)
Deck.shuffle_deck()
f = open("disadv.txt", "w")
sys.stdout = f
print ("damage\tcondition\tpierce")
j=0
for i in range(test_number):
	j=j+1
	#card = Deck.draw()
	card = Deck.draw2(base = base , adv= False)
	#card = Deck.draw2(base = base , adv= True)
	damage = 0
	if (card.name is '2x'):
		damage = (base+ card.modifier)* 2
	elif (card.name is'null'):
		damage = 0
	else:
		damage = base + card.modifier
	if (damage <0):
		damage = 0
	#print (damege ,"\t" ,card.condition)
	print ("%d\t%s\t%d" % (damage,card.condition,card.pierce))
	if (j == attack_per_turn):
		Deck.turn_end()
		j=0


sys.stdout = orig_stdout
f.close()
print ("disadvantage finish!")

