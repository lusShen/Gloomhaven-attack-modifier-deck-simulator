from itertools import chain

class Ability(dict):
	def __missing__(self, key):
		return 0


class Attack_modifier_card:
	def __init__(self, name='' ,modifier = 0 , condition = set(), ability = Ability() , roll = False, shuffle_marker = False, loss = False, multiplication = 1):
		self.name = name
		self.modifier = modifier 
		self.condition = condition #include wound, poison ... etc
		self.ability = ability #include bless x, curse x, pierce x, push x ...etc, any ability with a number
		self.roll = roll 
		self.shuffle_marker = shuffle_marker #a card with shuffle_marker cause the shuffle
		self.loss = loss #a card with loss won't back to the deck once it's drawn
		self.multiplication = multiplication # 2x = 2, null =0
		
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
		
		temp.multiplication = self.multiplication
		
		if (other.multiplication != 1):
			temp.multiplication = other.multiplication
		return temp

