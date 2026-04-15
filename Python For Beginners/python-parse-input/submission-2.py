from typing import List

def read_integers() -> List[int]:
    str_input = input()
    str_to_list = str_input.split(",")
    for char in str_to_list:
        str_to_list.append(int(char))
    return str_to_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
