import dreamland_generators as gen

Region = gen.AdventureLocation()

# TODO: function to format/print output
print(Region)

for route in Region.route_lines():
	print("\t" + route)

# Print out location descriptions
for location in Region.location_lines():
	print("\t" + location)

# Print out list of connections
for connection in Region.connection_lines():
	print("\t" + connection)



