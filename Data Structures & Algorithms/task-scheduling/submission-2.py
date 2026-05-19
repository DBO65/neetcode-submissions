class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letMap = {}
        for task in tasks:
            letMap[task] = letMap.get(task,0) + 1

        maxHeap = [-cnt for cnt in letMap.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time