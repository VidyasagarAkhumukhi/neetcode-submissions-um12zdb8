class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #  [10, 9, 8, 7 ,6, 6, 9]  h = 7

        # if len(piles) == h and max(piles) > h:
        #     return max(piles)

        l, r = 1, max(piles)
        res = r

        while l <= r:
            speed = (l + r) // 2
            totalTime = 0 

            for pile in piles:
                totalTime += math.ceil(pile / speed)
            
            if totalTime <= h:
                res = speed
                
                r = speed - 1
            else:
                l = speed + 1
        
        return res



        

        # speed = 1

        # while True:
        #     totalTime = 0

        #     for pile in piles:
        #         totalTime += math.ceil(pile / speed)

        #     if totalTime <= h:
        #         return speed
        #     speed += 1
        
        # return speed