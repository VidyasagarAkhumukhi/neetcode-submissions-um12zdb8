class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
            
        # sorting
        # if sorted(s) == sorted(t):
        #     return True
        # return False

        # return sorted(s) == return(t)

        # counting
        # if Counter(s) != Counter(t):
        #     return False
        # return True

        # return Counter(s) == Counter(t)
        

        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)

        # return countS == countT 

        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False
        
        # return True

        # if len(s) != len(t):
        #     return False

        # return sorted(s) == sorted(t)

        # return Counter(s) == Counter(t)

        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # return countS == countT


        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            count[char] = count.get(char, 0) - 1

        for val in count.values():
            if val != 0:
                return False
        return True  


    


