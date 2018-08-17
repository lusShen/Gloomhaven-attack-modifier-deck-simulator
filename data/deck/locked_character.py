from object.GH_AMC import Ability, Attack_modifier_card
from common_card import Basic_card

#Sun


#Triple_Arrow 


#Circles
#the coder haven't unlocked this class


#Eclipse
#the coder haven't unlocked this class


#Cthulhu


#Lightning
#the coder haven't unlocked this class


#Music Note
MusicNote_AMC={
	'+4' : Attack_modifier_card(name = '+4',modifier = 4),
	
	'+1_immobilize' : Attack_modifier_card(name = '+1 immobilize',modifier = 1 , condition = set(['immobilize'])),
	'+1_disarm' : Attack_modifier_card(name = '+1 disarm',modifier = 1 , condition = set(['disarm'])),
	'+2_wound' : Attack_modifier_card(name = '+2 wound',modifier = 2 , condition = set(['wound'])),
	'+2_poison' : Attack_modifier_card(name = '+2 poison',modifier = 2 , condition = set(['poison']))
	'+2_curse' : Attack_modifier_card(name = '+2 curse',modifier = 2 , ability = Ability([('curse',1)]))
	'+3_muddle' : Attack_modifier_card(name = '+3 muddle',modifier = 3 , condition = set(['muddle']))
	'stun' : Attack_modifier_card(name = '+0 stun',modifier = 0 , condition = set(['stun'])),
	
	'r_+1' : Attack_modifier_card(name = 'roll +1',modifier = 1 , roll=True),
	'r_curse' : Attack_modifier_card(name = 'roll curse',modifier = 0 , roll = True, ability = Ability([('curse',1)]))
}

#Face Mask
#the coder haven't unlocked this class



#Saw
Saw_AMC={
	'+2' : Attack_modifier_card(name = '+2',modifier = 2),
	
	'r_+2' : Attack_modifier_card(name = 'roll +2',modifier = 2 , roll=True),
	
	'+1_immobilize' : Attack_modifier_card(name = '+1 immobilize',modifier = 1 , condition = set(['immobilize'])),
	
	'r_wound' : Attack_modifier_card(name = 'roll wound',modifier = 0 , roll = True , condition = set(['wound'])),
	'r_stun' : Attack_modifier_card(name = 'roll stun',modifier = 0 , roll = True , condition = set(['stun'])),
	'r_heal3' : Attack_modifier_card(name = 'roll heal_3',modifier = 0 , roll = True, ability = Ability([('heal',3)])),
	
	'item' : Attack_modifier_card(name = 'item refresh',modifier = 0 , condition = set(['item refresh']))
}


#Triangle
#the coder haven't unlocked this class


#Two-Minis
#the coder haven't unlocked this class
