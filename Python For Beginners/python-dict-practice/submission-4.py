from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    outDict = {}
    count = 0

    for i in range(len(word)):
        if word[i] in outDict:
            count += 1
        outDict[word[i]] = count
    return outDict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
