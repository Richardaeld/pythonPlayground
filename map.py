from listsAndObjs import numList


def multiplyBy3 (x):
    return x * 3

result = list(map(multiplyBy3, numList))

result = [num for num in result if num % 2 == 0]

print(result)