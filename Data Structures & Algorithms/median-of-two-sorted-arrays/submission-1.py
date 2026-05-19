"""
- Two arays in ascending order
- when combined they create on array with two sorted sections
- The result is a float
- We can find the Max and Min in O(1)
- We can swap with O(1)
- 

Brute force combine the arrays then find the median but that is O(n)

Think:
size of merged array = m + n 
medain = value at (m + n)/ 2 (either rounded up or + 1 if odd and 
the ((l + h)/2)) if even.

Len(combinedArr) = 5 + 8 = 13
partition = 6

if we take the mid point of the smaller arr (3) we know that the 
partition of the larger array will be 3 elements long to to create 
a valid partition.

we can validate if the partition is correct by checking that the end
of each mid point is smaller then the next element in the alternate array
as it should be to match the corresponding ascending order.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total//2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1 
        while True:
            i = (l + r) // 2
            j = half - 1 - i - 1 # Working with index not count so have to offset by two for the two arrays (the total array and B)

            A_MaxLeft = A[i] if i >= 0 else float("-infinity")
            A_MinRight = A[i + 1] if (i + 1) < len(A) else float("infinity")
            B_MaxLeft = B[j] if j >= 0 else float("-infinity")
            B_MinRight = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if A_MaxLeft <= B_MinRight and B_MaxLeft <= A_MinRight:
                if total % 2 == 1:
                    return min(A_MinRight, B_MinRight)
                return (max(A_MaxLeft, B_MaxLeft) + min(A_MinRight, B_MinRight)) / 2
            elif A_MaxLeft > B_MinRight:
                r = i - 1
            else:
                l = i + 1
            

            

                  
        