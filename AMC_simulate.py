
import sys





from object.GH_AMC_class_deck import AMC_class_deck
from object.GH_AMC_deck import AMC_deck
from data.deck.basic_deck import Basic_deck
from data.card.common_card import Basic_card
from data.deck.base_character import basic_class
from data.deck.locked_character import locked_class
from custom.deck import custom_class
import copy
import setting


orig_stdout = sys.stdout




def add_curse(deck):
	
	if (setting.curse_count>0):
		deck.add_card(Basic_card['curse'])
		setting.curse_count -= 1

def add_bless(deck):
	if (setting.bless_count>0):
		deck.add_card(Basic_card['bless'])
		setting.bless_count -= 1


def Deck_simulation(deck ,filename, adv = 0):
	Deck = copy.deepcopy(deck)
	Deck.shuffle_deck()
	f = open(filename, "w")
	damageCount=0
	
	sys.stdout = f
	print ("damage\tcondition\tability")
	attack=0
	
	#Deck.check_perk('remove_two_-1')
	#Deck.check_perk('replace_one_-1_w_one_+1')
	#Deck.check_perk('add_two_+1')
	#Deck.check_perk('add_two_+1')
	#Deck.check_perk('add_one_+3')
	#Deck.check_perk('add_three_r_push1')
	#Deck.check_perk('add_three_r_push1')
	#Deck.check_perk('add_two_r_pierce3')
	#Deck.check_perk('add_one_r_stun')
	#Deck.check_perk('add_one_r_stun')
	#Deck.check_perk('add_one_r_disarm_one_r_muddle')
	#Deck.check_perk('add_one_r_target')
	#Deck.check_perk('add_one_r_target')
	#Deck.check_perk('add_one_+1_shield1')
	#Deck.check_perk('ignore_negative_item_add_one_+1')
	if type(Deck)==AMC_class_deck:
		Deck.check_all()
	
	for i in range(setting.test_number):
		
		attack += 1
		
		if (adv==0):
			card = Deck.draw()
		elif(adv ==-1):
			card = Deck.draw2(base_damage = setting.base_damage , adv= False)
		elif(adv ==1):
			card = Deck.draw2(base_damage = setting.base_damage , adv= True)
		
		damage = (setting.base_damage + card.modifier) * card.multiplication
		if (damage <0):
			damage = 0
		
		damageCount += damage
		#print (damege ,"\t" ,card.condition)
		condition = '\t'.join(card.condition)
#		if (len(card.condition) >0):
#			condition = card.condition
#		else:
#			condition = ""
		ability = '\t'.join( k+':'+str(v) for k,v in card.ability.items())
#		if (len(card.ability) >0):
#			ability = card.ability
#		else:
#			ability = "";
		print ("%d\t%s\t%s" % (damage,condition,ability))
		if (setting.attack_per_turn > 0 and attack % setting.attack_per_turn == 0):
			Deck.turn_end()

		if (setting.attack_per_curse > 0 and attack % setting.attack_per_curse == 0):
			add_curse(Deck)
			
		if (setting.attack_per_bless > 0 and attack % setting.attack_per_bless == 0):
			add_bless(Deck)

	sys.stdout = orig_stdout
	
	print(damageCount / setting.test_number)
	
	f.close()

setting.init()

if setting.test_class in basic_class:
	character = AMC_class_deck(perks = basic_class[setting.test_class])
elif setting.test_class in locked_class:
	character = AMC_class_deck(perks = locked_class[setting.test_class])
elif setting.test_class in custom_class:
	character = AMC_class_deck(perks = custom_class[setting.test_class])
else:
	character = Basic_deck



Deck_simulation(deck = character, adv = 0  , filename = 'normal.txt')
print ("normal finish!")

setting.init()

Deck_simulation(deck = character, adv = 1 , filename = 'adv.txt')
print ("advantage finish!")

setting.init()

Deck_simulation(deck = character, adv = -1 , filename = 'disadv.txt')
print ("disadvantage finish!")