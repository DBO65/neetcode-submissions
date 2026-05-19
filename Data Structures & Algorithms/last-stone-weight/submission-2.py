class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        
        for i, n in enumerate(stones):
            stones[i] = -n
        heapq.heapify(stones)

        while len(stones) >= 2:
            x = -(heapq.heappop(stones))
            y = -(heapq.heappop(stones))
            diff = abs(x-y)
            heapq.heappush(stones, -diff)
        
        return -stones[0]
        

        