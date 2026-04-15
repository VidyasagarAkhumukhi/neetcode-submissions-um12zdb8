from typing import List

def read_integers() -> List[int]:
    str_input = input()
    str_to_list = str_input.split(",")
    list_new = []
    for char in str_to_list:
        list_new.append(int(char))
    return list_new

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
