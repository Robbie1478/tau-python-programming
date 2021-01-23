fruits = ["Apple", "Organge", "Apple", "Pear", "Cherry", "Apple", "Grape"]
years = [3, "1998", 2.5, 987, "1984"]

#checking membership in a list
print("Apple" in fruits) #will be True
print("Apples" in fruits) #will be False

print(fruits.count("Apple"))
#because python uses zero based, the 1st position will be at 0
print(fruits.index("Apple"))

fruits =["Peaches", "Pears", "Apples"]

years = [3, "1998", 2.5, 987, "1994"]

print(fruits, years)

fruits.append("Oranges")
print(fruits)

fruits.extend(years)
print(fruits)

fruits.remove("Peaches")
print(fruits)

fruits.pop(0)
print(fruits)

fruits.pop(-1)
print(fruits)

numbers = [5, 1928, 4, 17, 68]
numbers.sort()
print (numbers)
