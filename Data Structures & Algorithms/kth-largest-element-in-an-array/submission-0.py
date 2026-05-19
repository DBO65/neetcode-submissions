class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        big = []
        cnt, sol = 0, 0
        heapq.heapify(big)

        for num in nums:
            num = -num
            heapq.heappush(big, num)

        while cnt < k:
            sol = heapq.heappop(big)
            cnt += 1
        
        return -sol



