class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Conceptual:
        1) We are searching for a target in a sorted array that has been rotated n times.
        2) When rotating the elements at the end of the array must now be at the start.T
        3) The nums length, values and size of values are not massive. 
        4) We must return -1 if we cannot find it (not finding it is a possibility)
        5) We Should first see what section the target is in
        6) Since the array is split into two sorted sections, there will be 2 smallest and largest
        
        A) Which section is target in 
        We figure that out by seeing whether or not the mid value is larger than the left, if it is 
        then it is one of two sorted sections. If the target is larger than the mid or smaller than the left
        portion of that section it is not in the section.

        2) binary search for target in that section
        If the target is not in the left section we should updat the left pointer to be in side the right section 
        and vice versa.

        This boils down to checking if the section is the bigger than left and smaller than mid to see if 
        it fits in the left section and smaller than right bigger than mid for the right section
        

        """

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l)//2
            if nums[m] == target:
                return m

            elif nums[l] <= nums[m]:
                if target <= nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1

            else:
                if target >= nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
