class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Stacks work because we only really need to care about the top/ most recently added
        elements.  So create a stack for speed and positon. 

        lets say distance to target = target - position
        time to target = DTT/speed

        we just make a set of the time to targets add all TTT to it.

        We also have to account for catch ups which can only occur if a car has more DTT 
        but less TTT then a car ahead of it.

        I dont see how to to account for catch up in O(n) time but if I sort I can do it in 
        O(nlogn) instead of O(n^2)

        """
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        