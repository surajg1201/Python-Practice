def swapList(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp
    return newList


newList = [1, 2, 3, 4, 5]
# print(swapList(newList))


def swap(list, el1, el2):

    temp = list[el1]
    list[el1] = list[el2]
    list[el2] = temp
    return list


print(swap(newList, 3, 2))
