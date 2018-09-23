from object.GH_AMC import Ability, Attack_modifier_card



#Sun
Sun_AMC={
	'0' : Attack_modifier_card(name = '0',modifier = 0),
	'+1' : Attack_modifier_card(name = '+1',modifier = 1),
	'+2' : Attack_modifier_card(name = '+2',modifier = 2),
	
	'r_+1' : Attack_modifier_card(name = 'roll +1',modifier = 1 , roll=True),
	'r_heal1' : Attack_modifier_card(name = 'roll heal_1',modifier = 0 , roll = True, ability = Ability([('heal',1)])),
	'r_stun' : Attack_modifier_card(name = 'roll stun',modifier = 0 , roll = True , condition = set(['stun'])),
	'r_light' : Attack_modifier_card(name = 'roll light',modifier = 0 , roll = True , condition = set(['light'])),
	'r_shield1' : Attack_modifier_card(name = 'roll shield_1',modifier = 0 , roll = True, ability = Ability([('shield',1)])),
}

#Triple_Arrow 
TripleArrow_AMC={
	'+1' : Attack_modifier_card(name = '+1',modifier = 1),
	'+2' : Attack_modifier_card(name = '+2',modifier = 2),
	
	'r_+1' : Attack_modifier_card(name = 'roll +1',modifier = 1 , roll=True),
	'r_muddle' : Attack_modifier_card(name = 'roll muddle',modifier = 0 , roll = True , condition = set(['muddle'])),
	'r_pierce3' : Attack_modifier_card(name = 'roll pierce_3',modifier = 0 , roll = True, ability = Ability([('pierce',3)])),
	'r_stun' : Attack_modifier_card(name = 'roll stun',modifier = 0 , roll = True , condition = set(['stun'])),
	'r_target' : Attack_modifier_card(name = 'roll add target',modifier = 0 , roll = True , ability = Ability([('add target',1)])),
	'item' : Attack_modifier_card(name = 'item refresh',modifier = 0 , condition = set(['item refresh']))
}

#Circles
Circles_AMC={
	'0' : Attack_modifier_card(name = '0',modifier = 0),
	'+1' : Attack_modifier_card(name = '+1',modifier = 1),
	'+2' : Attack_modifier_card(name = '+2',modifier = 2),
	
	'r_wound' : Attack_modifier_card(name = 'roll wound',modifier = 0 , roll = True , condition = set(['wound'])),
	'r_poison' : Attack_modifier_card(name = 'roll poison',modifier = 0 , roll = True , condition = set(['poison'])),
	'r_heal1' : Attack_modifier_card(name = 'roll heal_1',modifier = 0 , roll = True, ability = Ability([('heal',1)])),
	
	'r_fire' : Attack_modifier_card(name = 'roll fire',modifier = 0 , roll = True , condition = set(['fire'])),
	'r_air' : Attack_modifier_card(name = 'roll air',modifier = 0 , roll = True , condition = set(['air'])),
	'r_dark' : Attack_modifier_card(name = 'roll dark',modifier = 0 , roll = True , condition = set(['dark'])),
	'r_earth' : Attack_modifier_card(name = 'roll earth',modifier = 0 , roll = True , condition = set(['earth']))

}


#Eclipse
Eclipse_AMC={
	'+1' : Attack_modifier_card(name = '+1',modifier = 1),
	
	'-1_dark' : Attack_modifier_card(name = '-1 dark',modifier = -1 , condition = set(['dark'])),
	'+1_dark' : Attack_modifier_card(name = '+1 dark',modifier = 1 , condition = set(['dark'])),
	'+1_invisible' : Attack_modifier_card(name = '+1 invisible',modifier = 1 , condition = set(['invisible'])),
	
	'r_muddle' : Attack_modifier_card(name = 'roll muddle',modifier = 0 , roll = True , condition = set(['muddle'])),
	'r_heal1' : Attack_modifier_card(name = 'roll heal_1',modifier = 0 , roll = True, ability = Ability([('heal',1)])),
	'r_curse' : Attack_modifier_card(name = 'roll curse',modifier = 0 , roll = True, ability = Ability([('curse',1)])),
	'r_target' : Attack_modifier_card(name = 'roll add target',modifier = 0 , roll = True , ability = Ability([('add target',1)]))
}

#Cthulhu
Cthulhu_AMC={
	'0' : Attack_modifier_card(name = '0',modifier = 0),
	'+1' : Attack_modifier_card(name = '+1',modifier = 1),
	'+2' : Attack_modifier_card(name = '+2',modifier = 2),
	
	'+1_air' : Attack_modifier_card(name = '+1 air',modifier = 1 , condition = set(['air'])),
	
	'r_poison' : Attack_modifier_card(name = 'roll poison',modifier = 0 , roll = True , condition = set(['poison'])),
	'r_curse' : Attack_modifier_card(name = 'roll curse',modifier = 0 , roll = True, ability = Ability([('curse',1)])),
	'r_immobilize' : Attack_modifier_card(name = 'roll immobilize',modifier = 0 , roll = True , condition = set(['immobilize'])),
	'r_stun' : Attack_modifier_card(name = 'roll stun',modifier = 0 , roll = True , condition = set(['stun']))
}

#Lightning
Lightning_AMC={
	'+1' : Attack_modifier_card(name = '+1',modifier = 1),
	
	'+2_fire' : Attack_modifier_card(name = '+2 fire',modifier = 2 , condition = set(['fire'])),
	
	'r_+2' : Attack_modifier_card(name = 'roll muddle',modifier = 2 , roll = True ),
	'r_wound' : Attack_modifier_card(name = 'roll wound',modifier = 0 , roll = True , condition = set(['wound'])),
	'r_stun' : Attack_modifier_card(name = 'roll stun',modifier = 0 , roll = True , condition = set(['stun'])),	
	'r_+1_disarm' : Attack_modifier_card(name = 'roll +1 disarm',modifier = 1 , roll = True , condition = set(['disarm'])),
	'r_heal1' : Attack_modifier_card(name = 'roll heal_1',modifier = 0 , roll = True, ability = Ability([('heal',1)]))
}


#Music Note
MusicNote_AMC={
	'+4' : Attack_modifier_card(name = '+4',modifier = 4),
	
	'+1_immobilize' : Attack_modifier_card(name = '+1 immobilize',modifier = 1 , condition = set(['immobilize'])),
	'+1_disarm' : Attack_modifier_card(name = '+1 disarm',modifier = 1 , condition = set(['disarm'])),
	'+2_wound' : Attack_modifier_card(name = '+2 wound',modifier = 2 , condition = set(['wound'])),
	'+2_poison' : Attack_modifier_card(name = '+2 poison',modifier = 2 , condition = set(['poison'])),
	'+2_curse' : Attack_modifier_card(name = '+2 curse',modifier = 2 , ability = Ability([('curse',1)])),
	'+3_muddle' : Attack_modifier_card(name = '+3 muddle',modifier = 3 , condition = set(['muddle'])),
	'stun' : Attack_modifier_card(name = '+0 stun',modifier = 0 , condition = set(['stun'])),
	
	'r_+1' : Attack_modifier_card(name = 'roll +1',modifier = 1 , roll=True),
	'r_curse' : Attack_modifier_card(name = 'roll curse',modifier = 0 , roll = True, ability = Ability([('curse',1)]))
}

#Face Mask
FaceMask_AMC={
	'+1' : Attack_modifier_card(name = '+1',modifier = 1),
	
	'+2_muddle' : Attack_modifier_card(name = '+2 muddle',modifier = 2 , condition = set(['muddle'])),
	'+1_poison' : Attack_modifier_card(name = '+1 poison',modifier = 1 , condition = set(['poison'])),
	'+1_wound' : Attack_modifier_card(name = '+1 wound',modifier = 1 , condition = set(['wound'])),	
	'+1_immobilize' : Attack_modifier_card(name = '+1 immobilize',modifier = 1 , condition = set(['immobilize'])),
	'stun' : Attack_modifier_card(name = '+0 stun',modifier = 0 , condition = set(['stun'])),
	
	'r_+1' : Attack_modifier_card(name = 'roll +1',modifier = 1 , roll=True),
	'r_target' : Attack_modifier_card(name = 'roll add target',modifier = 0 , roll = True , ability = Ability([('add target',1)]))
}



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
Triangle_AMC={
	'+1' : Attack_modifier_card(name = '+1',modifier = 1),
	'+2' : Attack_modifier_card(name = '+2',modifier = 2),
	
	'fire' : Attack_modifier_card(name = '+0 fire',modifier = 0 , condition = set(['fire'])),
	'ice' : Attack_modifier_card(name = '+0 ice',modifier = 0 , condition = set(['ice'])),
	'air' : Attack_modifier_card(name = '+0 air',modifier = 0 , condition = set(['air'])),
	'earth' : Attack_modifier_card(name = '+0 earth',modifier = 0 , condition = set(['earth'])),
	
	'+1_push1' : Attack_modifier_card(name = '+1 push_1',modifier = 1, ability = Ability([('push',1)])),
	'+1_wound' : Attack_modifier_card(name = '+1 wound',modifier = 1 , condition = set(['wound'])),
	'stun' : Attack_modifier_card(name = '+0 stun',modifier = 0 , condition = set(['stun'])),
	'target' : Attack_modifier_card(name = '+0 add target',modifier = 0 , ability = Ability([('add target',1)]))
}


#Two-Minis
#the coder haven't unlocked this class
