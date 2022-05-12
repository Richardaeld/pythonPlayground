array = [1,23,5,6,4,4,4,3,2,2,3,1,1,6,7,7,8,8,8,9,10,10,14]
array1 = [1,23,5,6,4,4,4,3,2,2,3,1,1,6,7,7,8,8,8,9,10,10,14]

print(array)


# set
newArray = list(set(array1))
print(newArray)


# loop
# def loopRev(array):
#     arrayLength = len(array)
#     newArray = []
#     for num in range(0, arrayLength):
#         minValue = min(array)
#         if len(newArray) == 0:
#             newArray.append(minValue)
#         elif minValue != newArray[-1]:
#             newArray.append(minValue)

#         array.remove(minValue)
#     print(newArray)

# loopRev(array)


def loopRev():
    array2 = []
    for i in array:
        if i not in array2:
            array2.append(i)

