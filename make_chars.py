"""Randomly generate NPCs and PCs"""

import char_generators as char_gen
from read_data import Dice

for x in range(20):
	print("\n" + str(x+1) + ".\t" + str(char_gen.Character().get_long_desc()))

print("\nThe party consists of:")

for x in range(6):
	print("\n" + str(x+1) + ".\t" + str(char_gen.PC().get_char_desc()))


