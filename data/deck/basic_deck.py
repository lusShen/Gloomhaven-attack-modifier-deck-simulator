from data.card.common_card import Basic_card
from object.GH_AMC_deck import AMC_deck

Basic_deck = AMC_deck(
	list([
		Basic_card['critical'],
		Basic_card['miss'],
		
		Basic_card['0'],
		Basic_card['0'],
		Basic_card['0'],
		Basic_card['0'],
		Basic_card['0'],
		Basic_card['0'],
		
		Basic_card['+1'],
		Basic_card['+1'],
		Basic_card['+1'],
		Basic_card['+1'],
		Basic_card['+1'],
		
		Basic_card['-1'],
		Basic_card['-1'],
		Basic_card['-1'],
		Basic_card['-1'],
		Basic_card['-1'],
		
		Basic_card['+2'],
		Basic_card['-2']
	])
)

