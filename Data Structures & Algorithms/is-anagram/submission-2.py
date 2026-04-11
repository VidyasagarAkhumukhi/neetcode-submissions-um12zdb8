class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)

        # hashmap, TC = O(n), SC = O(n)
        
        # if len(s) != len(t):
        #     return False
    
        # anaMapS = {}
        # anaMapT = {}

        # for i in s:
        #     if i in anaMapS:
        #         anaMapS[i] += 1
        #     anaMapS[i] = 1
        # for i in t:
        #     if i in anaMapT:
        #         anaMapT[i] += 1
        #     anaMapT[i] = 1
        
        # if anaMapS == anaMapT:
        #     return True
        # return False
               
        
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        if countS == countT:
            return True
        return False
            


