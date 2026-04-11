class Solution:

    def encode(self, strs: List[str]) -> str:
        outE = ""

        for s in strs:
            outE +=  str(len(s)) + '#' + s 
        return outE

    def decode(self, s: str) -> List[str]:
        outD, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            outD.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return outD



