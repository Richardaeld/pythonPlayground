# Create a list 1 - 10
numList = [num for num in range(1, 11)]
print('Whole list',  numList)


# filter out evens
evenList = [num for num in numList if num % 2 == 0]
print(evenList)


# filter out odds
oddList = [num for num in numList if num % 2 != 0]
print(oddList)