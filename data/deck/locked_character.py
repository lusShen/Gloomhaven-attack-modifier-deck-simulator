from data.card.common_card import Basic_card
from data.card.locked_character import *
locked_class={
	#Sun
	'Sun':{
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
	'TripleArrow':{
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
	#the coder haven't unlocked this class


	#Cthulhu
	'Cthulhu':{
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
	#the coder haven't unlocked this class


	#Music Note
	'MusicNote':{
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
	'Saw':{
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
		
		'add_one_r_stun':{
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
	#the coder haven't unlocked this class


	#Two-Minis
	#the coder haven't unlocked this class
}