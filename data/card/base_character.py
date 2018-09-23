from object.GH_AMC import Ability, Attack_modifier_card
from data.card.common_card import Basic_card

#Brute
Brute_AMC={
	'+1' : Attack_modifier_card(name = '+1',modifier = 1),
	'+3' : Attack_modifier_card(name = '+3',modifier = 3),
	
	'r_push1' : Attack_modifier_card(name = 'roll push_1',modifier = 0, roll = True, ability = Ability([('push',1)])),
	'r_pierce3' : Attack_modifier_card(name = 'roll pierce_3',modifier = 0 , roll = True, ability = Ability([('pierce',3)])),
	'r_stun' : Attack_modifier_card(name = 'roll stun',modifier = 0 , roll = True , condition = set(['stun'])),
	'r_disarm' : Attack_modifier_card(name = 'roll disarm',modifier = 0 , roll = True , condition = set(['disarm'])),
	'r_muddle' : Attack_modifier_card(name = 'roll muddle',modifier = 0 , roll = True , condition = set(['muddle'])),
	'r_target' : Attack_modifier_card(name = 'roll add target',modifier = 0 , roll = True , ability = Ability([('add target',1)])),
	
	'+1_shield1' : Attack_modifier_card(name = '+1 shield_3',modifier = 1 , ability = Ability([('shield',1)]))
}

#Tinkerer
Tinkerer_AMC={
	'0' : Attack_modifier_card(name = '0',modifier =  0),
	'+1' : Attack_modifier_card(name = '+1',modifier = 1),
	'+3' : Attack_modifier_card(name = '+3',modifier = 3),
	
	'r_fire' : Attack_modifier_card(name = 'roll fire',modifier = 0 , roll = True , condition = set(['fire'])),
	'r_muddle' : Attack_modifier_card(name = 'roll muddle',modifier = 0 , roll = True , condition = set(['muddle'])),
	
	'+1_wound' : Attack_modifier_card(name = '+1 wound',modifier = 1 , condition = set(['wound'])),
	'+1_immobilize' : Attack_modifier_card(name = '+1 immobilize',modifier = 1 , condition = set(['immobilize'])),
	'+1_heal2' : Attack_modifier_card(name = '+1 heal_2',modifier = 1 , ability = Ability([('heal',2)])),
	'target' : Attack_modifier_card(name = 'add target',modifier = 0 , ability = Ability([('add target',1)]))
}

#Spellweaver
Spellweaver_AMC={
	'+1' : Attack_modifier_card(name = '+1',modifier =  1),
	
	'stun' : Attack_modifier_card(name = '+0 stun',modifier = 0 , condition = set(['stun'])),
	'+1_wound' : Attack_modifier_card(name = '+1 wound',modifier = 1 , condition = set(['wound'])),
	'+1_immobilize' : Attack_modifier_card(name = '+1 immobilize',modifier = 1 , condition = set(['immobilize'])),
	'+1_curse' : Attack_modifier_card(name = '+1 curse',modifier = 1 , ability = Ability([('curse',1)])),
	'+2_fire' : Attack_modifier_card(name = '+2 fire',modifier = 2 , condition = set(['fire'])),
	'+2_ice' : Attack_modifier_card(name = '+2 ice',modifier = 2 , condition = set(['ice'])),

	'r_earth' : Attack_modifier_card(name = 'roll earth',modifier = 0 , roll = True , condition = set(['earth'])),
	'r_air' : Attack_modifier_card(name = 'roll air',modifier = 0 , roll = True , condition = set(['air'])),
	'r_light' : Attack_modifier_card(name = 'roll light',modifier = 0 , roll = True , condition = set(['light'])),
	'r_dark' : Attack_modifier_card(name = 'roll dark',modifier = 0 , roll = True , condition = set(['dark']))
}

#Scoundrel
Scoundrel_AMC={
	'0' : Attack_modifier_card(name = '0',modifier =  0),
	'+1' : Attack_modifier_card(name = '+1',modifier =  1),
	'+2' : Attack_modifier_card(name = '+2',modifier =  2),
	
	'r_+1' : Attack_modifier_card(name = 'roll +1',modifier = 1 , roll=True),
	'r_pierce3' : Attack_modifier_card(name = 'roll pierce_3',modifier = 0 , roll = True, ability = Ability([('pierce',3)])),
	'r_poison' : Attack_modifier_card(name = 'roll poison',modifier = 0 , roll = True , condition = set(['poison'])),
	'r_muddle' : Attack_modifier_card(name = 'roll muddle',modifier = 0 , roll = True , condition = set(['muddle'])),
	'r_invisible' : Attack_modifier_card(name = 'roll invisible',modifier = 0 , roll = True , condition = set(['invisible'])),
}

#Cragheart
Cragheart_AMC={
	'+1' : Attack_modifier_card(name = '+1',modifier =  1),
	'+2' : Attack_modifier_card(name = '+2',modifier =  2),
	'-2' : Attack_modifier_card(name = '-2',modifier = -2),
	
	'+1_immobilize' : Attack_modifier_card(name = '+1 immobilize',modifier = 1 , condition = set(['immobilize'])),
	'+2_muddle' : Attack_modifier_card(name = '+2 muddle',modifier = 2 , condition = set(['muddle'])),
	
	'r_push2' : Attack_modifier_card(name = 'roll push_2',modifier = 0, roll = True, ability = Ability([('push',2)])),
	'r_earth' : Attack_modifier_card(name = 'roll earth',modifier = 0 , roll = True , condition = set(['earth'])),
	'r_air' : Attack_modifier_card(name = 'roll air',modifier = 0 , roll = True , condition = set(['air']))
}

#Mindthief
Mindthief_AMC={
	'0' : Attack_modifier_card(name = '0',modifier =  0),
	'+2' : Attack_modifier_card(name = '+2',modifier =  2),
	
	'+2_ice' : Attack_modifier_card(name = '+2 ice',modifier = 2 , condition = set(['ice'])),
	
	'r_+1' : Attack_modifier_card(name = 'roll +1',modifier = 1 , roll=True),
	'r_pull1' : Attack_modifier_card(name = 'roll pull_1',modifier = 0, roll = True, ability = Ability([('pull',1)])),
	'r_muddle' : Attack_modifier_card(name = 'roll muddle',modifier = 0 , roll = True , condition = set(['muddle'])),
	'r_immobilize' : Attack_modifier_card(name = 'roll immobilize',modifier = 0 , roll = True , condition = set(['immobilize'])),
	'r_stun' : Attack_modifier_card(name = 'roll stun',modifier = 0 , roll = True , condition = set(['stun'])),
	'r_disarm' : Attack_modifier_card(name = 'roll disarm',modifier = 0 , roll = True , condition = set(['disarm']))
}



