from typing import List

def read_integers() -> List[int]:
    string = input()

    stringList = string.split(",")
    # print(stringList)
    integerList = []

    for char in stringList:
        integerList.append(char)

    return integerList

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
