class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Conceptual: We are searching for a target in a sorted array that has been rotated
        n times. When rotating the elements must be put at the end of teh array must now
        ne put at the start. The nums length, values and size of values are not massive. We must
        return -1 if we cannot find it (not finding it is a possibility)

        What we know: We know it starts off as a srted array and then gets rotated (changed). We 
        know that when it is changed the values at the end get placed in to the front.  We know
        the target of what we are looking for. We know that the target is not nescesarrily in the 
        array.

        Intuition: Seeing that the elements at the end or the array are pushed to the front of 
        the array when rotated the array has two sorted portions.  What we should first do is 
        identify which portion of the array the target is in.  We can do this by first seeing if
        the element at position l is greater than the target, if it is that means the section 
        
        1) Which section is target in 
        2) binary search for target in that section


        """

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l)//2
            if nums[m] == target:
                return m

            elif nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
