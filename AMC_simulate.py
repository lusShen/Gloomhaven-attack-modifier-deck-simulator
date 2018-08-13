
import sys



from GH_AMC import Ability, Attack_modifier_card
from GH_AMC_deck import AMC_deck

orig_stdout = sys.stdout
test_number = 1000000
attack_per_turn = 1
base_damage = 1


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
	card_rollp1
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