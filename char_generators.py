import random
from read_data import * 

# Define ability scores
abilities = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

# Define generation of ability scores
def get_classic_ability_scores():
	"""Generates ability scores the classic way (3d6 down the line)"""
	return sum(Dice(n=3).roll())

def get_knave_ability_scores():
	"""Generates ability scores per Knave 1e (lowest of 3d6, down the line)"""
	return min(Dice(n=3).roll())

def pick_class(ability_scores):
	"""Pick a class based on highest ability score"""
	abilities = list(ability_scores.keys())
	scores = list(ability_scores.values())
	highest_ability = abilities[scores.index(max(scores))]

	if highest_ability == 'STR':
		pc_class = 'Fighter'
	elif highest_ability == 'DEX':
		pc_class = 'Thief'
	elif highest_ability == 'INT':
		pc_class = 'Sorceror'
	elif highest_ability == 'WIS':
		pc_class = 'Mystic'
	else:
		pc_class = random.choice(['Fighter','Thief','Sorceror','Mystic'])

	return pc_class


# Create dictionaries of male/female surnames by culture
names_dict = {
	'the Concordat': {
		'Male': feedstock['Concordat_Male'],
    	'Female': feedstock['Concordat_Female'],
    	'Surname': feedstock['Concordat_Surname'],
	},
	'the Imperium': {
		'Male': feedstock['Imperium_Male'],
		'Female': feedstock['Imperium_Female'],
		'Surname': feedstock['Imperium_Surname'],
	},
	'the Inner Sea': {
		'Male': feedstock['InnerSea_Male'],
    	'Female': feedstock['InnerSea_Female'],
		'Descriptor': proper_noun
	},
	'the Northlands': {
		'Male': feedstock['Northlands_Male'],
    	'Female': feedstock['Northlands_Female'],
		'Descriptor': feedstock['Descriptor']
	}, 
	'Adelaura': {
		'Male': feedstock['Adelaura_Male'],
		'Female': feedstock['Adelaura_Female'],
		'Surname': feedstock['Adelaura_Surname'],
	}
}	

# Pronouns determine which list to pick first name from
pronouns_dict = {
	'He': 'Male',
	'She': 'Female',
	'They': random.choice(['Male','Female'])
}

class Character:
	"""
	Creates a character. 
	Age, name, gender, and culture and determined randomly, or can be specified. 
	Names are generated based on culture. 
	Profession, descriptors, and traits are also generated randomly.
	"""
	def __init__(self, age = None, pronoun = None, culture = None):
		if age:
			self.age = age
		else:
			self.age = random.choices(feedstock["Age"], weights=(4,3,2,1))[0]
		if pronoun:
			self.pronoun = pronoun
		else:
			self.pronoun = random.choices(("He","She","They"), weights = (.45, .45, .10))[0]
		self.gender = pronouns_dict.get(self.pronoun)
		if culture:
			self.culture = culture
		else:
			self.culture = random.choice(("the Concordat","the Imperium","the Inner Sea","the Northlands","Adelaura"))
	
		self.first_name = random.choice(names_dict.get(self.culture).get(self.gender))
		
		# Set up name (Inner Sea and Northlands use honorifics)
		if self.culture == "the Inner Sea":
			self.last_name = "of " + random.choice(names_dict.get(self.culture).get("Descriptor"))
		elif self.culture == "the Northlands":
			self.last_name = "the " + random.choice(names_dict.get(self.culture).get("Descriptor"))
		else:
			self.last_name = random.choice(names_dict.get(self.culture).get("Surname"))
		
		# Make full name
		self.full_name = self.first_name + " " + self.last_name	

		# Get profession
		self.profession = random.choice(feedstock["Honest_Labor"] + feedstock["Skilled_Labor"] + feedstock["The_Book"] + feedstock["The_Sword"] + feedstock["The_Streets"] + feedstock["The_Palace"] + feedstock["The_Art"] + feedstock["The_Faith"] + feedstock["The_Outcasts"])

		# Get descriptors
		self.physical = random.choice(feedstock["Hair"] + feedstock["Eyes"] + feedstock["Hands"] + feedstock["Clothes"] + feedstock["Speech"] + feedstock["Body"] + feedstock["Accessories"] + feedstock["Face"])
		self.demeanour = random.choice(feedstock["Demeanour"])
		self.personality = random.choice(feedstock["Personality"])
		self.trait = random.choice(feedstock["Trait"])


	def __str__(self):
		return(self.full_name)

	def get_long_desc(self):
		return(f"{self.full_name}, {self.age} {self.profession.lower()} from {self.culture} ({self.physical.lower()}, {self.demeanour.lower()}, {self.personality.lower()}). {self.pronoun} {self.trait}.")

class PC(Character):
	"""Creates a player character. Inherits from Character class."""
	def __init__(self, age = None, pronoun = None, culture = None, system = 'Classic', level = 1):
		super().__init__()
		self.occ_adj = random.choice(feedstock["Occupation_adjective"])
		self.downfall = random.choice(feedstock["Downfall"])
		self.system = system
		self.level = level
		self.stats = {}
		self.XP = 0
		self.next_lvl_xp = 1000

		for stat in abilities:
			if system == 'Knave':
				self.stats[stat] = get_knave_ability_scores()
			else:
				self.stats[stat] = get_classic_ability_scores()

		self.char_class = pick_class(self.stats)

	def get_char_desc(self):
		return(
			f"{self.full_name}"
			f"\n\tLv. {self.level} {self.char_class}"
			f"\n\t{self.occ_adj} {self.profession.lower()} from {self.culture}"
			f"\n\t{self.physical}, {self.demeanour.lower()}, {self.personality.lower()}"
			f"\n\tBrought low by {self.downfall.lower()}, {self.pronoun.lower()} {self.trait.lower()}"
			f"\n\t{self.stats}"
		)

	def saving_throw(self, ability):
		"""Make a saving throw based on a specific ability score (if given)"""
		roll = random.randint(1,20)
		if roll <= self.stats[ability]:
			return True
		else:
			return False

	def gain_XP(self, xp):
		"""Add XP to current XP total and check whether it exeeds level threshold. If so, level up!"""
		self.XP += xp

		while self.XP >= self.next_lvl_xp:
			self.level += 1
			self.next_lvl_xp = self.next_lvl_xp + self.level * 1000
			
		else:
			return(f"{self.full_name} is Lvl. {self.level}. {self.XP}/{self.next_lvl_xp} to next level.")


	def get_stats(self):
		for ability, score in self.stats.items():
			print(f"\t{ability} {score}")


class Party():
	"""
	Generates an adventuring party consisting of some number of PCs.
	Party size can be specified; if not, it is determined randomly.
	"""
	def __init__(self, n = int()):
		if n > 0:
			self.n = abs(n)
		elif n < 0:
			raise ValueError("Party size (n) must be greater than zero!")
		else:
			self.n = random.randint(3,6)
		self.members = []
		for i in range(self.n):
			self.members.append(PC())

	def __str__(self):
		member_names = []
		for i in range(self.n):
			member_names.append(str(self.members[i]))
		return(str(member_names))

	def list_members(self):
		for i in range(self.n):
			print(self.members[i].get_char_desc())
		
	def allocate_xp(self, xp):
		self.xp = int(xp)
		self.xp_per_char = int(self.xp / self.n)
		for i in range(self.n):
			self.members[i].gain_XP(self.xp_per_char)