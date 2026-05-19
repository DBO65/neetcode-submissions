class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letMap = {}
        for task in tasks:
            letMap[task] = letMap.get(task,0) + 1

        maxHeap = [-cnt for cnt in letMap.values()]
        heapq.heapify(maxHeap)

        cycle = 0
        q = deque()  # pairs of [-cnt, idleTime]

        while maxHeap or q:
            cycle += 1
            if not maxHeap:
                cycle = q[0][1]
            else:
                letCnt = 1 + heapq.heappop(maxHeap)
                if letCnt:
                    q.append([letCnt, cycle + n])
            if q and q[0][1] == cycle:
                heapq.heappush(maxHeap, q.popleft()[0])
        return cycle