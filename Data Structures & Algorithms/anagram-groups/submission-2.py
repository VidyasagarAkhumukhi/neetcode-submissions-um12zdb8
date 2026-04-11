class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # out = []

        # for i in range(len(strs)):
        #     strs[i].sort()
        #     for j in range( i + 1, len(strs)):
        #         if len(set(strs[i])) == len(strs[j]):
        #             out = [[strs[i], strs[j]]]
        
        # return out

        out = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for singleC in s:
                count[ord(singleC) - ord('a')] += 1

            out[tuple(count)].append(s)
        
        return list(out.values())