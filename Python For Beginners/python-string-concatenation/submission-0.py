def concatenate(s1: str, s2: str) -> str:
    sout = s1 + s2
    if len(sout) > 10:
        return "Too long!"
    return sout




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
