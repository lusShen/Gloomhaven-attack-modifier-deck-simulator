import os.path
import sys
import argparse
import setting

from object.GH_AMC_class_deck import AMC_class_deck
from object.AMC_simulator import Deck_simulation
from data.deck.basic_deck import Basic_deck
from data.deck.base_character import basic_class
from data.deck.locked_character import locked_class
from custom.deck import custom_class
from object.AMC_result_analyzer import AMC_result_analyzer

parser = argparse.ArgumentParser(description="run the simulation and analyze")
parser.add_argument("-n", dest="class_name", default="Basic_deck",
	help="the name of class you want to test")

parser.add_argument("-o", dest="output_path", default="result/",
	help="the path of output")
	
parser.add_argument("-curse", dest="curse", default=0,
	help="numbers of attacks per curse")
parser.add_argument("-bless", dest="bless", default=0,
	help="numbers of attacks per bless")

args = parser.parse_args()
test_class = args.class_name

if test_class in basic_class:
	character = AMC_class_deck(perks = basic_class[test_class])
elif test_class in locked_class:
	character = AMC_class_deck(perks = locked_class[test_class])
elif test_class in custom_class:
	character = AMC_class_deck(perks = custom_class[test_class])
else:
	character = Basic_deck

setting.init()
setting.attack_per_curse = int(args.curse)
setting.attack_per_bless = int(args.bless)

p = args.output_path + test_class
if (not os.path.isfile( p + '.txt')):
	Deck_simulation(deck = character, adv =  0  , filename = p + '.txt')

setting.init()
setting.attack_per_curse = int(args.curse)
setting.attack_per_bless = int(args.bless)
if (not os.path.isfile(p + '_advantage.txt')):
	Deck_simulation(deck = character, adv =  1  , filename = p + '_advantage.txt')

setting.init()
setting.attack_per_curse = int(args.curse)
setting.attack_per_bless = int(args.bless)
if (not os.path.isfile(p + '_disadvantage.txt')):
	Deck_simulation(deck = character, adv = -1  , filename = p + '_disadvantage.txt')

AMC_result_analyzer(
	p + '.txt',
	args.output_path +'analyze.txt',
	test_class
)
AMC_result_analyzer(
	p + '_advantage.txt',
	args.output_path +'analyze.txt',
	test_class + '_adv'
)
AMC_result_analyzer(
	p + '_disadvantage.txt',
	args.output_path +'analyze.txt',
	test_class + '_disadv'
)