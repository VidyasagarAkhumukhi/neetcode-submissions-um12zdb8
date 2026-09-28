from typing import List

def read_integers() -> List[int]:
    string = input()

    integerList = string.split(",")

    return integerList

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
