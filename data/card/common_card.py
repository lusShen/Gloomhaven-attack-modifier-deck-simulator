from object.GH_AMC import Ability, Attack_modifier_card

#basic cards
Basic_card = {
	'critical': Attack_modifier_card(name = '2x', shuffle_marker = True, multiplication = 2),
	'miss' : Attack_modifier_card(name = 'null',modifier = -999, shuffle_marker = True, multiplication = 0),
	'0' : Attack_modifier_card(name = '0'),
	'+1' : Attack_modifier_card(name = '+1',modifier = 1),
	'+2' : Attack_modifier_card(name = '+2',modifier = 2),
	'-1' : Attack_modifier_card(name = '-1',modifier = -1),
	'-2' : Attack_modifier_card(name = '-2',modifier = -2),
	'bless' : Attack_modifier_card(name = 'bless',multiplication = 2,loss = True),
	'curse' : Attack_modifier_card(name = 'curse',modifier = -999, multiplication = 0,loss = True)
}