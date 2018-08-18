from data.card.common_card import Basic_card
from data.card.base_character import *
basic_class={
	#Brute
	'Brute':{
		'remove_two_-1':{
			'available' : 1,
			'modification' : [
				(Basic_card['-1'],'r',2)
			]
		},
		
		'replace_one_-1_w_one_+1':{
			'available' : 1,
			'modification' : [
				(Basic_card['-1'],'r',1),
				(Brute_AMC['+1'],'a',1)
			]
		},
		
		'add_two_+1':{
			'available' : 2,
			'modification' : [
				(Brute_AMC['+1'],'a',2)
			]
		},
		
		'add_one_+3':{
			'available' : 1,
			'modification' : [
				(Brute_AMC['+3'],'a',1)
			]
		},

		
		'add_three_r_push1':{
			'available' : 2,
			'modification' : [
				(Brute_AMC['r_push1'],'a',3)
			]
		},
		
		'add_two_r_pierce3':{
			'available' : 1,
			'modification' : [
				(Brute_AMC['r_pierce3'],'a',2)
			]
		},
		
		'add_one_r_stun':{
			'available' : 2,
			'modification' : [
				(Brute_AMC['r_stun'],'a',1)
			]
		},
		
		'add_one_r_disarm_one_r_muddle':{
			'available' : 1,
			'modification' : [
				(Brute_AMC['r_disarm'],'a',1),
				(Brute_AMC['r_muddle'],'a',1)
			]
		},
		
		'add_one_r_target':{
			'available' : 2,
			'modification' : [
				(Brute_AMC['r_target'],'a',1)
			]
		},
		
		'add_one_+1_shield1':{
			'available' : 1,
			'modification' : [
				(Brute_AMC['+1_shield1'],'a',1)
			]
		},
		
		'ignore_negative_item_add_one_+1':{
			'available' : 1,
			'modification' : [
				(Brute_AMC['+1'],'a',1)
			]
		}
	},

	#Tinkerer
	'Tinkerer':{
		'remove_two_-1':{
			'available' : 2,
			'modification' : [
				(Basic_card['-1'],'r',2)
			]
		},
		
		'replace_one_-2_w_one_0':{
			'available' : 1,
			'modification' : [
				(Basic_card['-2'],'r',1),
				(Tinkerer_AMC['0'],'a',1)
			]
		},
		
		'add_two_+1':{
			'available' : 1,
			'modification' : [
				(Tinkerer_AMC['+1'],'a',2)
			]
		},
		
		'add_one_+3':{
			'available' : 1,
			'modification' : [
				(Tinkerer_AMC['+3'],'a',1)
			]
		},
		
		'add_two_r_fire':{
			'available' : 1,
			'modification' : [
				(Tinkerer_AMC['r_fire'],'a',2)
			]
		},
		
		'add_three_r_muddle':{
			'available' : 1,
			'modification' : [
				(Tinkerer_AMC['r_muddle'],'a',3)
			]
		},
		
		'add_one_+1_wound':{
			'available' : 2,
			'modification' : [
				(Tinkerer_AMC['+1_wound'],'a',1)
			]
		},
		
		'add_one_+1_immobilize':{
			'available' : 2,
			'modification' : [
				(Tinkerer_AMC['+1_immobilize'],'a',1)
			]
		},
		
		'add_one_+1_heal2':{
			'available' : 2,
			'modification' : [
				(Tinkerer_AMC['+1_heal2'],'a',1)
			]
		},
		
		'add_one_target':{
			'available' : 1,
			'modification' : [
				(Tinkerer_AMC['target'],'a',1)
			]
		},
		
		'ignore_negative_scenario':{
			'available' : 1,
			'modification' : [
				
			]
		}
	},

	#Spellweaver
	'Spellweaver':{
		
		'remove_four_0':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',4)
			]
		},
		
		'replace_one_-1_w_one_+1':{
			'available' : 2,
			'modification' : [
				(Basic_card['-1'],'r',1),
				(Spellweaver_AMC['+1'],'a',1)
			]
		},
		
		'add_two_+1':{
			'available' : 2,
			'modification' : [
				(Spellweaver_AMC['+1'],'a',2)
			]
		},
		
		'add_one_stun':{
			'available' : 1,
			'modification' : [
				(Spellweaver_AMC['stun'],'a',1)
			]
		},
		
		'add_one_+1_wound':{
			'available' : 1,
			'modification' : [
				(Spellweaver_AMC['+1_wound'],'a',1)
			]
		},
		
		'add_one_+1_immobilize':{
			'available' : 1,
			'modification' : [
				(Spellweaver_AMC['+1_immobilize'],'a',1)
			]
		},
		
		'add_one_+1_curse':{
			'available' : 1,
			'modification' : [
				(Spellweaver_AMC['+1_curse'],'a',1)
			]
		},
		
		'add_one_+2_fire':{
			'available' : 2,
			'modification' : [
				(Spellweaver_AMC['+2_fire'],'a',1)
			]
		},
		
		'add_one_+2_ice':{
			'available' : 2,
			'modification' : [
				(Spellweaver_AMC['+2_ice'],'a',1)
			]
		},
		
		'add_one_r_earth_one_r_air':{
			'available' : 1,
			'modification' : [
				(Spellweaver_AMC['r_earth'],'a',1),
				(Spellweaver_AMC['r_air'],'a',1)
			]
		},
		
		'add_one_r_light_one_r_dark':{
			'available' : 1,
			'modification' : [
				(Spellweaver_AMC['r_light'],'a',1),
				(Spellweaver_AMC['r_dark'],'a',1)
			]
		}
	},

	#Scoundrel
	'Scoundrel':{
		'remove_two_-1':{
			'available' : 2,
			'modification' : [
				(Basic_card['-1'],'r',2)
			]
		},
		
		'remove_four_0':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',4)
			]
		},
		
		'replace_one_-2_w_one_0':{
			'available' : 1,
			'modification' : [
				(Basic_card['-2'],'r',1),
				(Scoundrel_AMC['0'],'a',1)
			]
		},
		
		'replace_one_-1_w_one_+1':{
			'available' : 1,
			'modification' : [
				(Basic_card['-1'],'r',1),
				(Scoundrel_AMC['+1'],'a',1)
			]
		},
		
		'replace_one_0_w_one_+2':{
			'available' : 2,
			'modification' : [
				(Basic_card['0'],'r',1),
				(Scoundrel_AMC['+2'],'a',1)
			]
		},
		
		'add_two_r_+1':{
			'available' : 2,
			'modification' : [
				(Scoundrel_AMC['r_+1'],'a',2)
			]
		},
		
		'add_two_r_pierce3':{
			'available' : 1,
			'modification' : [
				(Scoundrel_AMC['r_pierce3'],'a',2)
			]
		},
		
		'add_two_r_poison':{
			'available' : 2,
			'modification' : [
				(Scoundrel_AMC['r_poison'],'a',2)
			]
		},
		
		'add_two_r_muddle':{
			'available' : 1,
			'modification' : [
				(Scoundrel_AMC['r_muddle'],'a',2)
			]
		},
		
		'add_one_r_invisible':{
			'available' : 1,
			'modification' : [
				(Scoundrel_AMC['r_invisible'],'a',1)
			]
		},
		
		'ignore_negative_scenario':{
			'available' : 1,
			'modification' : [
				
			]
		}
	},

	#Cragheart
	'Cragheart':{
		
		'remove_four_0':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',4)
			]
		},
		
		'replace_one_-1_w_one_+1':{
			'available' : 3,
			'modification' : [
				(Basic_card['-1'],'r',1),
				(Cragheart_AMC['+1'],'a',1)
			]
		},
		
		'add_two_+2_one_-2':{
			'available' : 1,
			'modification' : [
				(Cragheart_AMC['+2'],'a',2),
				(Cragheart_AMC['-2'],'a',1)
			]
		},
		
		'add_one_+1_immobilize':{
			'available' : 2,
			'modification' : [
				(Cragheart_AMC['+1_immobilize'],'a',1)
			]
		},
		
		'add_one_+2_muddle':{
			'available' : 2,
			'modification' : [
				(Cragheart_AMC['+2_muddle'],'a',1)
			]
		},
		
		'add_two_r_push2':{
			'available' : 1,
			'modification' : [
				(Cragheart_AMC['r_push2'],'a',2)
			]
		},
		
		'add_two_r_earth':{
			'available' : 2,
			'modification' : [
				(Cragheart_AMC['r_earth'],'a',2)
			]
		},
		
		'add_two_r_air':{
			'available' : 2,
			'modification' : [
				(Cragheart_AMC['r_air'],'a',2)
			]
		},
		
		'ignore_negative_item':{
			'available' : 1,
			'modification' : [
				
			]
		},
		
		'ignore_negative_scenario':{
			'available' : 1,
			'modification' : [
				
			]
		}
	},

	#Mindthief
	'Mindthief':{
		'remove_two_-1':{
			'available' : 2,
			'modification' : [
				(Basic_card['-1'],'r',2)
			]
		},
		'remove_four_0':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',4)
			]
		},
		
		'replace_two_+1_w_two_+2':{
			'available' : 1,
			'modification' : [
				(Basic_card['+1'],'r',2),
				(Mindthief_AMC['+2'],'a',2)
			]
		},
		
		'replace_one_-2_w_one_0':{
			'available' : 1,
			'modification' : [
				(Basic_card['-2'],'r',1),
				(Mindthief_AMC['0'],'a',1)
			]
		},
		
		'add_one_+2_ice':{
			'available' : 2,
			'modification' : [
				(Mindthief_AMC['+2_ice'],'a',1)
			]
		},
		
		'add_two_r_+1':{
			'available' : 2,
			'modification' : [
				(Mindthief_AMC['r_+1'],'a',2)
			]
		},
		
		'add_three_r_pull1':{
			'available' : 1,
			'modification' : [
				(Mindthief_AMC['r_pull1'],'a',3)
			]
		},
		
		'add_three_r_muddle':{
			'available' : 1,
			'modification' : [
				(Mindthief_AMC['r_muddle'],'a',3)
			]
		},
		
		'add_two_r_immobilize':{
			'available' : 1,
			'modification' : [
				(Mindthief_AMC['r_immobilize'],'a',2)
			]
		},
		
		'add_one_r_stun':{
			'available' : 1,
			'modification' : [
				(Mindthief_AMC['r_stun'],'a',1)
			]
		},
		
		'add_one_r_disarm_one_r_muddle':{
			'available' : 1,
			'modification' : [
				(Mindthief_AMC['r_disarm'],'a',1),
				(Mindthief_AMC['r_muddle'],'a',1)
			]
		},
		
		'ignore_negative_scenario':{
			'available' : 1,
			'modification' : [
				
			]
		}
	}


}
