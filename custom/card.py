from object.GH_AMC import Ability, Attack_modifier_card

#here are some custom cards sample


#custom
sample_AMC={
	'+1' : Attack_modifier_card(name = '+1',modifier = 1),
	
	'+1_air' : Attack_modifier_card(name = '+1 air',modifier = 1 , condition = set(['air'])),
	'+1_earth' : Attack_modifier_card(name = '+1 earth',modifier = 1 , condition = set(['earth'])),
	'+1_light' : Attack_modifier_card(name = '+1 light',modifier = 1 , condition = set(['light'])),
	'+1_dark' : Attack_modifier_card(name = '+1 dark',modifier = 1 , condition = set(['dark'])),
	
	'+1_wound' : Attack_modifier_card(name = '+1 wound',modifier = 1 , condition = set(['wound'])),
	'+1_poison' : Attack_modifier_card(name = '+1 poison',modifier = 1 , condition = set(['poison'])),
	'+2_muddle' : Attack_modifier_card(name = '+2 muddle',modifier = 2 , condition = set(['muddle'])),
	
	'r_heal1' : Attack_modifier_card(name = 'roll heal_1',modifier = 0 , roll = True, ability = Ability([('heal',1)]))
}

