# Declare a list variable

cities = ["Mumbai", "Ayodhya","Jaipur", "Pune", "Nashik" ]

print(cities)
print(type(cities))
print(cities[1])

# Adding element at the end of the list

cities.append("Chennai")
cities.append(True)
cities.append(False)

print(cities)

# Adding element at a particular index
cities.insert(3,  "Delhi")

print(cities)

# Removing element from the end of the list
cities.pop()
# Removing element by using the index
cities.pop(3)
cities.pop()

print(cities)

for city in cities:
    print("The Current Value is:")
    print(city)

print("Process completed")

countries = ["India","Russia","USA"]
for country in countries:
    print(country)

print("Process completed")
