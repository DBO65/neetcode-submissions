class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Parameters: Temps
        Returning an array of how many days after i until hotter day if no hotter the 0
        Not working with humongous sets
        Each index = ith day (0 = day 1 and etc)

        If we initialize the array to be 0 then we dont have to create an explecit base case condition
        for each element iterate till we find a hotter day but that could be 0(n^2)
        Instead what we could do is use a stack and for each day that ith day is > than the 
        the top of the stack we pop the stack and increment the count.  To find the day that it 
        corresponds to we can simply i - count + 1

        There could be O(1) space but the simplest answer to me is O(n) by using another stack to 
        represent temps
         

        '''
        stack = []
        sol = [0]*(len(temperatures))
        

        for i in range(len(temperatures)):
            count = 0
            j = i - 1
            while j >= 0 and temperatures[i] > temperatures[stack[j]]:
                tempIdx = stack[j]
                count += 1
                if sol[tempIdx] == 0:
                    sol[tempIdx] = count
                j -= 1
            stack.append(i)
        return sol
