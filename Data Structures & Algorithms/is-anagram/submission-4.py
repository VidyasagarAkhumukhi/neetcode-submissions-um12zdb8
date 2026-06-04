class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # sorting
        # if sorted(s) == sorted(t):
        #     return True
        # return False

        # counting
        # if counted(s) != counted(t):
        #     return False
        # return True

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT 

        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False
        
        # return True


    


