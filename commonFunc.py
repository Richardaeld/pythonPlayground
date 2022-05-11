# Zip
words = ['as', 'you', 'are']
counts = [1, 3, 5]

print("zip")
for word, count in zip(words, counts):
    print(word,count)
print()


# Type
print("type")
print(type(words))
print(type(counts))
print()


# Sum
print("sum")
counts = [1,1,1,1,3,3,3,3,5,5,5,5]
print(sum(counts))
print()


# Set
print("set")
print(set(counts))
print()


# List
print("list")
print(list(set(counts)))
print()


# Sorted
print("sorted")
counts = [2,3,1,9,7,4,6,54,4,5,4,4,9,1,2,7]
print(sorted(counts))
print()


# Range
print("range")
print(range(10))
print(range(1,10))
print(list(range(1,11)))
print()


# Round
print("round")
someFloat = 2.345890
print(round(someFloat,2))
print()


# Min and Max
print("min and max")
print(min(counts))
print(max(counts))
print()


# Map
print("map")
def map_Func(x):
    return x - 1
print(list(map(map_Func, counts)))
print()


# isinstance
print("isinstance")
diff_types = [True, 32, "32", "Ima string", 23.23, 0, False]
print(diff_types)
[print(item) for item in diff_types if isinstance(item, int)]
print()


# Help
print("help")
print(help(int))
print()
