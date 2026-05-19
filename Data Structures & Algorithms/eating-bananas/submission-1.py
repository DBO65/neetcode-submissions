class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        To brute force this i know that the max time i can take is h and the min time i can take
        is the number of piles (Because best case scenario i eat each pile in one go).  This means
        the answer must be in between these two piles and since im looking for an integer
        thats an easy binary search
        """
        maxK, minK = max(piles), 1
        sol = maxK
 
        while minK <= maxK:
            k = (maxK + minK) // 2 
            hrs = 0
            for pile in piles:
                hrs += -(pile//-k)

            if hrs <= h:
                sol = min(sol, k)
                maxK = k - 1 
            else:
                minK = k + 1

        return sol 


                

                    
                    


