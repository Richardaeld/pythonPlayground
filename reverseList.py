from datetime import datetime

orderedList = list(range(0, 21))


print(orderedList)

# orderedList.reverse()
# print(orderedList)


list2 = orderedList[::-1]
print("list 2", list2)


newOrderedList = []
orderedListLength = len(orderedList)
print(orderedListLength)
for num in range(0, orderedListLength):
    newOrderedList.append(orderedList.pop(-1))

print(newOrderedList)


print(datetime.now())