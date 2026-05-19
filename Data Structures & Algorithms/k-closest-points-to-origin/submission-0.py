class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distHeap, sol = [], [] 
        heapq.heapify(distHeap)

        for idx, cord in enumerate(points):
            dist = [(cord[0]**2 + cord[1]**2)**0.5, cord]
            heapq.heappush(distHeap, dist)

        for point in range(k):
            kDist = heapq.heappop(distHeap)
            sol.append(kDist[1])
        
        return sol
