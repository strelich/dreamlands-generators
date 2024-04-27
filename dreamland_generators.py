import random
from read_data import *
from creatures import Creature, Monster


# Regions
class Region:
	def __init__(self):
		self.adjective = random.choice(adjective)
		self.noun = random.choice(noun + proper_noun)
		self.terrain = random.choice(terrain)
		self.name = random.choice((
			f"{self.adjective} {self.terrain}",
			f"{self.terrain} of {self.noun}", 
			f"{self.adjective} {self.terrain} of {self.noun}"))
	
	def __str__(self):
		return self.name

# Routes
class Route:
	def __init__(self) -> None:
		self.adjective = random.choice(adjective)
		self.noun = random.choice(noun + proper_noun)
		self.path_type = random.choice(feedstock["Path_types"])
		self.name = random.choice((
			f"{self.adjective} {self.path_type}",
			f"{self.path_type} of {self.noun}", 
			f"{self.adjective} {self.path_type} of {self.noun}"))

	def __str__(self):
		return self.name

# Threats
class Threat:
	def __init__(self):
		self.threats = random.sample(feedstock["Things"], 2)
		self.name = self.threats[0] + " and " + self.threats[1]
	
	def __str__(self):
		return self.name


# Happenings
class Happening:
	def __init__(self):
		self.elements = random.sample(feedstock["Abulafia_domains"], 2) + random.sample(feedstock["Details_General"], 2)
	
	def __str__(self) -> str:
		return f"{self.elements[0]} and {self.elements[1].lower()}; {self.elements[2].lower()} and {self.elements[3].lower()}"

# Points
class Point:
	"""Generates a randomly-named point of interest"""
	def __init__(self):
		self.adjective = random.choice(adjective)
		self.noun = random.choice(noun + proper_noun)
		self.location = random.choice(locations)
		self.creature = Creature()
		self.rules = random.choice(feedstock["Rules_over"])
		self.happening = Happening()
		self.name = random.choices((
			f"{self.adjective} {self.location}",
			f"{self.location} of {self.noun}", 
			f"{self.adjective} {self.location} of {self.noun}"),weights=(.4,.4,.2))[0]

	def __str__(self):
		return self.name

	def full_description(self):
		return(
			f"The {self.name} ({self.rules} {self.creature})"
			f"\n{self.happening}"
			)

# Make some settlements!
class Settlement(Point):
	"""Generates a settlement. Inherits name-generation from Point"""
	def __init__(self):
		Point.__init__(self)
		self.size = random.choice(("Tiny","Small","Medium","Large","Massive"))
		self.features = random.choice(feedstock["Settlement_features"])
		self.people = random.sample(feedstock["People"], 2)
		self.leader = random.choice(feedstock['Leadership'])
		self.trouble = random.choice(feedstock['Trouble'])

	def full_description(self, md = False):
		self.md = md
		self.prefix = "\t\t\t"
		if self.md:
			self.prefix = ""
		
		return (
			f"The {self.name} ({self.size} settlement)"
			f"\n{self.prefix}{self.people[0].capitalize()}-{self.people[1].lower()}-folk, led by {self.leader.lower()}"
			f"\n{self.prefix}Contending with {self.trouble.lower()}"
			f"\n{self.prefix}{str(self.happening).capitalize()}"

		)

# Pulling it all together!
class AdventureLocation:
	def __init__(self, md = False):
		self.name = str(Region())
		self.size = random.choices(list(feedstock["Region_sizes"].keys()), weights = (.2, .2, .2, .2, .2))[0]
		self.happening = str(Happening())
		self.loc_nums = feedstock["Region_sizes"].get(self.size)
		self.routes = []
		for y in range(random.randrange(self.loc_nums[0],self.loc_nums[1])):
			self.routes.append(Route())
		self.locations = []
		for y in range(random.randrange(self.loc_nums[0],self.loc_nums[1])):
			self.locations.append(Point())
		for y in range(random.randrange(self.loc_nums[0],self.loc_nums[1])):
			self.locations.append(Settlement())
		self.md = md
		self.headers = ["","\t","\t\t","\t\t\t"]
		if self.md:
			self.headers = ["\n# ", "\n## ", "\n### ", "\n  - "]

	def __str__(self):
		return (
			f"{self.headers[0]}The {self.name} ({self.size} region)"
	  		f"\n{self.happening}"
		)

	def list_routes(self):
		print("\n" + self.headers[1] + "Routes:\n")
		for i in range(len(self.routes)):
			print(f"{self.headers[2]}{self.routes[i]}")

	def list_points(self):
		print("\n" + self.headers[1] + "Locations:\n")
		for i in range(len(self.locations)):
			print(f"{self.headers[2]}{self.locations[i].full_description()}")

	def connections(self):
		print("\n" + self.headers[1] + "Connections:\n")
		for i in range(len(self.locations)):
			pair = random.sample(self.locations, 2)
			relation = random.choice(feedstock["Point_relationships"])
			print(f"{self.headers[2]}{pair[0]} --> {pair[1]} ({relation})")
			