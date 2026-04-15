def add_two_numbers() -> int:
    str_inp = input()
    list_str = str_inp.split(",")
    list_add = []
    for num in list_str:
        list_add.append(int(num))
    for num in list_add:
        num += num
    return num
    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
