import json
import random

# Load data from json file
with open("feedstock.json") as input_file:
	feedstock = json.load(input_file)  # data is a dict now

# Make combo lists
adjective = feedstock["Adjective"] + feedstock["Both"]
noun = feedstock["Noun"]+ feedstock["Both"]
proper_noun = random.sample(
	feedstock["Invisible_cities"] + 
	feedstock["Mongolian_cities"] + 
	feedstock["Persian_cities"] + 
	feedstock["Lovecraft_cities"], 
	50) # Take subset to keep balance of proper vs. improper
terrain = (
	feedstock["Terrain_Coastal"] + 
	feedstock["Terrain_Wastes"] + 
	feedstock["Terrain_Mountainous"] + 
	feedstock["Terrain_Flat"] + 
	feedstock["Terrain_Wet"] + 
	feedstock["Terrain_Wooded"]
	)
locations = (
	feedstock["Locations_Exotic"] + 
	feedstock["Locations_Natural"] + 
	feedstock["Locations_Monument"] + 
	feedstock["Locations_Underground"] + 
	feedstock["Locations_Faith"] + 
	feedstock["Locations_Civilized"] + 
	feedstock["Locations_War"]
	)

# Directions
directions = random.sample(feedstock["Directions"], 8)

# Define dice
class Dice():
	"""
	Simulates rolling n d-sided dice. Defaults to 1d6. 
	Returns a list of results, one for each die.
	"""

	def __init__(self, n = 1, d = 6):
		self.n = n
		self.d = d
		
	def roll(self):
		dice = [None] * self.n
		for die in range(self.n):
			roll = random.randint(1,self.d)
			dice[die] = roll
		return dice


