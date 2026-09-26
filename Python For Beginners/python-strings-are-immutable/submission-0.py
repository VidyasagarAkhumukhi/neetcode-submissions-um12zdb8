def remove_fourth_character(word: str) -> str:
    newStr = word[:2] + word[4:]   
    return newStr

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
