from data.card.common_card import Basic_card
from custom.card import *


custom_class={
	#sample
	'sample':{
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
		
		'replace_one_-1_w_one_+1_air':{
			'available' : 1,
			'modification' : [
				(Basic_card['-1'],'r',1),
				(sample_AMC['+1_air'],'a',1)
			]
		},
		
		'replace_one_-1_w_one_+1_earth':{
			'available' : 1,
			'modification' : [
				(Basic_card['-1'],'r',1),
				(sample_AMC['+1_earth'],'a',1)
			]
		},
		
		'replace_one_-1_w_one_+1_light':{
			'available' : 1,
			'modification' : [
				(Basic_card['-1'],'r',1),
				(sample_AMC['+1_light'],'a',1)
			]
		},
		
		'replace_one_-1_w_one_+1_dark':{
			'available' : 1,
			'modification' : [
				(Basic_card['-1'],'r',1),
				(sample_AMC['+1_air'],'a',1)
			]
		},
		
		'add_two_r_heal1':{
			'available' : 2,
			'modification' : [
				(sample_AMC['r_heal1'],'a',2)
			]
		},
		
		'add_one_+1_wound':{
			'available' : 2,
			'modification' : [
				(sample_AMC['+1_wound'],'a',1)
			]
		},
		
		'add_one_+1_poison':{
			'available' : 2,
			'modification' : [
				(sample_AMC['+1_poison'],'a',1)
			]
		},
		
		'add_one_+2_muddle':{
			'available' : 1,
			'modification' : [
				(sample_AMC['+2_muddle'],'a',1)
			]
		},
		
		'ignore_negative_item_add_one_+1':{
			'available' : 1,
			'modification' : [
				(sample_AMC['+1'],'a',1)
			]
		},
		
		'ignore_negative_scenario_add_one_+1':{
			'available' : 1,
			'modification' : [
				(sample_AMC['+1'],'a',1)
			]
		}
	}
}