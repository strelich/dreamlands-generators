"""Scratchpad for random generation of adventuring parties"""
import char_generators as gen

party = gen.Party()

print("\n\nList names")

print(party)

print("\n\nList members")

for desc in party.member_descriptions():
    print(desc)

print("\nAnd some XP...")


party.allocate_xp(20000)

for desc in party.member_descriptions():
    print(desc)

print("\n\nPrint out stats")

party.members[0].get_stats()

