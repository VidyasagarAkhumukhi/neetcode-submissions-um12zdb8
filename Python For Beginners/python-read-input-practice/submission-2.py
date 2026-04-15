def add_two_numbers() -> int:
    str_inp = input()
    list_str = str_inp.split(",")
    list_add = []
    total = 0
    for num in list_str:
        list_add.append(int(num))
    for num in list_add:
        total += num
        
    return total
    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
