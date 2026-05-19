class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        So it is rotated when the end of the list is brought to the front and every other number 
        is incremented by 1.  I am going to first do the brute force solution which is to check
        if the next item in the list is larger than the last if it isn't I have my answer because
        that must be the start of the list and therefore the min. that gives me an  O(n) solution.

        For O(log n) What im gonna do is first use binary search for the position of the max of 
        array. I will know it is the max of the array if the next element after it is less
        than itself. Once i find the max I should only have to increment by one to find the min.
        """

        l, r = 0, len(nums) - 1

        sol = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                sol = min(sol, nums[l])
                break

            m = (l + r) // 2
            sol = min(sol, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return sol

        
