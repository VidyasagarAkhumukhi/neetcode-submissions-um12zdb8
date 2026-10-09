class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        carPair = [(p, s) for p, s in zip(position, speed)]
        carPair.sort(reverse = True)
        timeStack = []

        for p, s in carPair:
            timeStack.append((target - p) / s)

            if len(timeStack) >= 2 and timeStack[-1] <= timeStack[-2]:
                timeStack.pop()

        return len(timeStack)