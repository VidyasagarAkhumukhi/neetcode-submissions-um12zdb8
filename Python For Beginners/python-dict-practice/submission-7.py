from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    outDict = {}
    
    for char in word:
        if char not in outDict:
            outDict[char] = 0
        outDict[char] += 1
    return outDict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
