# Dreamlands Random Generators

Random generators for my TTRPG campaign, inspired by Lovecraft's Dreamlands (natch) and Lieber's Lankhmar. Started as an exercise to practice OOP, grew into its own thing.

## Overview

1. `feedstock.json` stores raw data
2. `read_data.py` loads this data into a dictionary of lists
3. `creatures.py`, `dreamland_generators.py`, and `char_generators.py` define classes/functions to generate characters, locations, &c.
4. `make_chars.py`, `make_party.py`, and `make_adventure.py` output characters, adventuring parties, and adenture regions, respectively.

## To Do

- Create functions to format results (plain text, Markdown, &c)
- Add random map generation
- Add Markov chains name generation
- Make web application