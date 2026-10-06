class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = {} # elements value -> count

        freqCount = [[] for i in range(len(nums) + 1)]

        for ele in nums:
            freqMap[ele] = freqMap.get(ele, 0) + 1
        
        for ele, index in freqMap.items():
            freqCount[index].append(ele)
        
        res = []
        for i in range(len(freqCount)-1, 0, -1):
            for num in freqCount[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        

        

            
