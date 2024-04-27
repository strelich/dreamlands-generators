"""Scratchpad for random generation of adventuring parties"""
import char_generators as gen

party = gen.Party()

print("\n\nList names")

print(party)

print("\n\nList members")

party.list_members()

print("\nAnd some XP...")


party.allocate_xp(20000)

party.list_members()

print("\n\nPrint out stats")

party.members[0].get_stats()

