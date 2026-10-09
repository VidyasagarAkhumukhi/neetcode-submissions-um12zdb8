class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carDet = [(p, s) for p, s in zip(position, speed)]
        carDet.sort(reverse = True)

        fleetStack = []

        for p, s in carDet:
            fleetStack.append((target - p) / s)
            if len(fleetStack) >= 2 and fleetStack[-1] <= fleetStack[-2]:
                fleetStack.pop()
        
        return len(fleetStack)