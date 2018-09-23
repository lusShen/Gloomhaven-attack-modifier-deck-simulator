from data.card.common_card import Basic_card
from data.card.locked_character import *
locked_class={
	#Sun
	'Sunkeeper':{
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
				(Sun_AMC['0'],'a',1)
			]
		},
		
		'replace_one_0_w_one_+2':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',1),
				(Sun_AMC['+2'],'a',1)
			]
		},
		
		'add_two_r_+1':{
			'available' : 2,
			'modification' : [
				(Sun_AMC['r_+1'],'a',2)
			]
		},
		
		'add_two_r_heal1':{
			'available' : 2,
			'modification' : [
				(Sun_AMC['r_heal1'],'a',2)
			]
		},
		
		'add_one_r_stun':{
			'available' : 1,
			'modification' : [
				(Sun_AMC['r_stun'],'a',1)
			]
		},
		
		'add_two_r_light':{
			'available' : 2,
			'modification' : [
				(Sun_AMC['r_light'],'a',2)
			]
		},
		
		'add_two_r_shield1':{
			'available' : 1,
			'modification' : [
				(Sun_AMC['r_shield1'],'a',2)
			]
		},
		
		'ignore_negative_item_add_two_+1':{
			'available' : 1,
			'modification' : [
				(Sun_AMC['+1'],'a',2)
			]
		},
		
		'ignore_negative_scenario':{
			'available' : 1,
			'modification' : [
				
			]
		}
	},

	#Triple_Arrow 
	'Quartermaster':{
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
		
		'replace_one_0_w_one_+2':{
			'available' : 2,
			'modification' : [
				(Basic_card['0'],'r',1),
				(TripleArrow_AMC['+2'],'a',1)
			]
		},
		
		'add_two_r_+1':{
			'available' : 2,
			'modification' : [
				(TripleArrow_AMC['r_+1'],'a',2)
			]
		},
		
		'add_three_r_muddle':{
			'available' : 1,
			'modification' : [
				(TripleArrow_AMC['r_muddle'],'a',3)
			]
		},
		
		'add_two_r_pierce3':{
			'available' : 1,
			'modification' : [
				(TripleArrow_AMC['r_pierce3'],'a',2)
			]
		},
		
		'add_one_r_stun':{
			'available' : 1,
			'modification' : [
				(TripleArrow_AMC['r_stun'],'a',1)
			]
		},
		
		'add_one_r_target':{
			'available' : 1,
			'modification' : [
				(TripleArrow_AMC['r_target'],'a',1)
			]
		},
		
		'add_one_item':{
			'available' : 3,
			'modification' : [
				(TripleArrow_AMC['item'],'a',1)
			]
		},
		
		'ignore_negative_item_add_two_+1':{
			'available' : 1,
			'modification' : [
				(TripleArrow_AMC['+1'],'a',2)
			]
		}
	},

	#Circles
	#the coder haven't unlocked this class


	#Eclipse
	'Nightshroud':{
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
		
		'add_one_-1_dark':{
			'available' : 2,
			'modification' : [
				(Eclipse_AMC['-1_dark'],'a',1)
			]
		},
		
		'replace_one_-1_dark_w_one_one_+1_dark':{
			'available' : 2,
			'modification' : [
				(Eclipse_AMC['-1_dark'],'r',1),
				(Eclipse_AMC['+1_dark'],'a',1)
			]
		},
		
		'add_one_+1_invisible':{
			'available' : 2,
			'modification' : [
				(Eclipse_AMC['+1_dark'],'a',1)
			]
		},
		
		'add_three_r_muddle':{
			'available' : 2,
			'modification' : [
				(Eclipse_AMC['r_muddle'],'a',3)
			]
		},
		
		'add_two_r_heal1':{
			'available' : 1,
			'modification' : [
				(Eclipse_AMC['r_heal1'],'a',2)
			]
		},
		
		'add_two_r_curse':{
			'available' : 1,
			'modification' : [
				(Eclipse_AMC['r_curse'],'a',2)
			]
		},
		
		'add_one_r_target':{
			'available' : 1,
			'modification' : [
				(Eclipse_AMC['r_target'],'a',1)
			]
		},

		'ignore_negative_scenario_add_two_+1':{
			'available' : 1,
			'modification' : [
				(Eclipse_AMC['+1'],'a',2)
			]
		}
	},


	#Cthulhu
	'Plagueherald':{
		'replace_one_-2_w_one_0':{
			'available' : 1,
			'modification' : [
				(Basic_card['-2'],'r',1),
				(Cthulhu_AMC['0'],'a',1)
			]
		},
		
		'replace_one_-1_w_one_+1':{
			'available' : 2,
			'modification' : [
				(Basic_card['-1'],'r',1),
				(Cthulhu_AMC['+1'],'a',1)
			]
		},
		
		'replace_one_0_w_one_+2':{
			'available' : 2,
			'modification' : [
				(Basic_card['0'],'r',1),
				(Cthulhu_AMC['+2'],'a',1)
			]
		},
		
		'add_two_+1':{
			'available' : 1,
			'modification' : [
				(Cthulhu_AMC['+1'],'a',2)
			]
		},
		
		'add_one_+1_air':{
			'available' : 3,
			'modification' : [
				(Cthulhu_AMC['+1_air'],'a',1)
			]
		},
		
		'add_three_r_poison':{
			'available' : 1,
			'modification' : [
				(Cthulhu_AMC['r_poison'],'a',3)
			]
		},
		
		'add_two_r_curse':{
			'available' : 1,
			'modification' : [
				(Cthulhu_AMC['r_curse'],'a',2)
			]
		},

		'add_two_r_immobilize':{
			'available' : 1,
			'modification' : [
				(Cthulhu_AMC['r_immobilize'],'a',2)
			]
		},
		
		'add_one_r_stun':{
			'available' : 2,
			'modification' : [
				(Cthulhu_AMC['r_stun'],'a',1)
			]
		},
		
		'ignore_negative_scenario_add_one_+1':{
			'available' : 1,
			'modification' : [
				(Cthulhu_AMC['+1'],'a',1)
			]
		}
	},

	#Lightning
	'Berserker':{
		'remove_two_-1':{
			'available' : 1,
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
		
		'replace_one_-1_w_one_+1':{
			'available' : 2,
			'modification' : [
				(Basic_card['-1'],'r',1),
				(Lightning_AMC['+1'],'a',1)
			]
		},
		
		'replace_one_0_w_one_r_+2':{
			'available' : 2,
			'modification' : [
				(Basic_card['0'],'r',1),
				(Lightning_AMC['r_+2'],'a',1)
			]
		},
		
		'add_two_r_wound':{
			'available' : 2,
			'modification' : [
				(Lightning_AMC['r_wound'],'a',2)
			]
		},
		
		'add_one_r_stun':{
			'available' : 2,
			'modification' : [
				(Lightning_AMC['r_stun'],'a',1)
			]
		},
		
		'add_one_r_+1_disarm':{
			'available' : 2,
			'modification' : [
				(Lightning_AMC['r_+1_disarm'],'a',1)
			]
		},
		
		'add_two_r_heal1':{
			'available' : 1,
			'modification' : [
				(Lightning_AMC['r_heal1'],'a',2)
			]
		},
		
		'add_one_+2_fire':{
			'available' : 2,
			'modification' : [
				(Lightning_AMC['+2_fire'],'a',1)
			]
		},
		
		'ignore_negative_item':{
			'available' : 1,
			'modification' : [
			
			]
		}
	},


	#Music Note
	'Soothsinger':{
		'remove_two_-1':{
			'available' : 2,
			'modification' : [
				(Basic_card['-1'],'r',2)
			]
		},
	
		'remove_one_-2':{
			'available' : 1,
			'modification' : [
				(Basic_card['-2'],'r',1)
			]
		},
		
		'replace_two_+1_w_one_+4':{
			'available' : 2,
			'modification' : [
				(Basic_card['+1'],'r',2),
				(MusicNote_AMC['+4'],'a',1)
			]
		},
		
		'replace_one_0_w_one_+1_immobilize':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',1),
				(MusicNote_AMC['+1_immobilize'],'a',1)
			]
		},
		
		'replace_one_0_w_one_+1_disarm':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',1),
				(MusicNote_AMC['+1_disarm'],'a',1)
			]
		},
		
		'replace_one_0_w_one_+2_wound':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',1),
				(MusicNote_AMC['+2_wound'],'a',1)
			]
		},
		
		'replace_one_0_w_one_+2_poison':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',1),
				(MusicNote_AMC['+2_poison'],'a',1)
			]
		},
		
		'replace_one_0_w_one_+2_curse':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',1),
				(MusicNote_AMC['+2_curse'],'a',1)
			]
		},
		
		'replace_one_0_w_one_+3_muddle':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',1),
				(MusicNote_AMC['+3_muddle'],'a',1)
			]
		},
		
		'replace_one_-1_w_one_stun':{
			'available' : 1,
			'modification' : [
				(Basic_card['-1'],'r',1),
				(MusicNote_AMC['stun'],'a',1)
			]
		},
		
		'add_three_r_+1':{
			'available' : 1,
			'modification' : [
				(MusicNote_AMC['r_+1'],'a',3)
			]
		},
		
		'add_two_r_curse':{
			'available' : 2,
			'modification' : [
				(MusicNote_AMC['r_curse'],'a',2)
			]
		}
	},

	#Face Mask
	#the coder haven't unlocked this class



	#Saw
	'Sawbones':{
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
		
		'replace_one_0_w_one_+2':{
			'available' : 2,
			'modification' : [
				(Basic_card['0'],'r',1),
				(Saw_AMC['+2'],'a',1)
			]
		},
		
		'add_one_r_+2':{
			'available' : 2,
			'modification' : [
				(Saw_AMC['r_+2'],'a',1)
			]
		},
		
		'add_one_+1_immobilize':{
			'available' : 2,
			'modification' : [
				(Saw_AMC['+1_immobilize'],'a',1)
			]
		},
		
		'add_two_r_wound':{
			'available' : 2,
			'modification' : [
				(Saw_AMC['r_wound'],'a',2)
			]
		},
		
		'add_one_r_stun':{
			'available' : 1,
			'modification' : [
				(Saw_AMC['r_stun'],'a',1)
			]
		},
		
		'add_one_r_heal3':{
			'available' : 2,
			'modification' : [
				(Saw_AMC['r_heal3'],'a',1)
			]
		},
		
		'add_one_item':{
			'available' : 1,
			'modification' : [
				(Saw_AMC['item'],'a',1)
			]
		}
	},

	
	#Triangle
	'Elmentalist':{
		'remove_two_-1':{
			'available' : 2,
			'modification' : [
				(Basic_card['-1'],'r',2)
			]
		},
		
		'replace_one_-1_w_one_+1':{
			'available' : 1,
			'modification' : [
				(Basic_card['-1'],'r',1),
				(Triangle_AMC['+1'],'a',1)
			]
		},
		
		'replace_one_0_w_one_+2':{
			'available' : 2,
			'modification' : [
				(Basic_card['0'],'r',1),
				(Triangle_AMC['+2'],'a',1)
			]
		},
		
		'add_three_fire':{
			'available' : 1,
			'modification' : [
				(Triangle_AMC['fire'],'a',3)
			]
		},
		
		'add_three_ice':{
			'available' : 1,
			'modification' : [
				(Triangle_AMC['ice'],'a',3)
			]
		},
		
		'add_three_air':{
			'available' : 1,
			'modification' : [
				(Triangle_AMC['air'],'a',3)
			]
		},
		
		'add_three_earth':{
			'available' : 1,
			'modification' : [
				(Triangle_AMC['earth'],'a',3)
			]
		},
		
		'replace_two_0_w_one_fire_one_earth':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',2),
				(Triangle_AMC['fire'],'a',1),
				(Triangle_AMC['earth'],'a',1)
			]
		},

		'replace_two_0_w_one_ice_one_air':{
			'available' : 1,
			'modification' : [
				(Basic_card['0'],'r',2),
				(Triangle_AMC['ice'],'a',1),
				(Triangle_AMC['air'],'a',1)
			]
		},
		
		'add_two_+1_push1':{
			'available' : 1,
			'modification' : [
				(Triangle_AMC['+1_push1'],'a',2)
			]
		},
		
		'add_one_+1_wound':{
			'available' : 1,
			'modification' : [
				(Triangle_AMC['+1_wound'],'a',1)
			]
		},
		
		'add_one_stun':{
			'available' : 1,
			'modification' : [
				(Triangle_AMC['stun'],'a',1)
			]
		},
		
		'add_one_add target':{
			'available' : 1,
			'modification' : [
				(Triangle_AMC['target'],'a',1)
			]
		}
	},


	#Two-Minis
	#the coder haven't unlocked this class
}