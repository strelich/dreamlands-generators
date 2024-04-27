import random
from read_data import *


class Creature:
	def __init__(self):
		self.descriptor = random.choice(feedstock["Descriptor"])
		self.type = random.choice(feedstock["Type"])
		self.name = random.choice(
			feedstock["Akkadian_gods"]+
			feedstock["Greek_gods"]+
			feedstock["Egyptian_gods"]+
			feedstock["Aztec_gods"]
			)
	
	def __str__(self) -> str:
		form1 = (f"{self.name}, the {self.descriptor} {self.type}")
		form2 = (f"{self.descriptor} {self.type} {self.name}")
		return random.choice([form1, form2])

class Monster:
	def __init__(self):
		self.essence = random.choice(feedstock["Essence"])
		self.form = random.choice(feedstock["Form"])
		self.special = random.choice(feedstock["Special"])
		self.effect = random.choice(feedstock["Effects"])
		self.hd = min(Dice(n=3,d=10).roll())
	
	def __str__(self) -> str:
		return f"{self.essence} {self.form.lower()} (HD {self.hd})\n\tSpecial: {self.special}\n\tAbility: {self.effect}\n"
	
for i in range(10):
	print(Creature())