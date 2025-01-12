states = ["Alabama", "Alaska", "Arizona", "Arkansas"]
cities = ["Mobile", "Anchorage", "Phoenix", "Jacksonville" ]

print(states[0])

print(states[-1])

states.append("California")

print(states[-1])

states.append(["California"])

print(states[-1])

print("Index Error")

#print(states[6])

print("Nested Lists")

combined_list = [states, cities]

print(f"The combined list looks like this {combined_list}.")

#extracting the list
print(combined_list[1])

#extracting the value from a nested list
print(combined_list[1][1])