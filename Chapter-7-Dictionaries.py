stuff = {"food": 15, "energy": 100, "enemies": 3}

#print(stuff.get("food"))

#prints the key and the value, key value pair
#print(stuff.items())

#print the keys
#print(stuff.keys())

#allows you to pop that last item in the dictionary
#print(stuff.popitem())

#print(stuff)

'''
print(stuff.setdefault("food"))
print(stuff)
#lets you add to the dictionary, in this case it adds a new key value pair of "friends", 123
print(stuff.setdefault("friends", 123))
print(stuff)
'''

#update the stuff dictionary with new_items dictionary
new_items = {"rock": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)

new_items = {"rock": 2, "arrows": 10}
stuff.update(new_items)
print(stuff)

#allows you to update and add to the dictionary at the same time
stuff.update(food = 399, cookies = 9)
print(stuff)