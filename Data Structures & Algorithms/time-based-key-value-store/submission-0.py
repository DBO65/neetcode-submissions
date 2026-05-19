"""
- Store Multiple values at same key at specified timestamps
- Retrieve key value at timestamp
- Timestamps strictly increasing
- If timestamped value isn't there show most recent value
- If there are no most recent values, returns ""



Brute Force:
Hashmap to initialize, append the timestamp : value pair to a list containing
all pairs for a key and then just run through the list and see what time stamp 
matches if none do the just print the value of the highest timestamp.

Ideally:
Hashmap containing list for the Time map so we can append the 
value : timestamp pairs (tuples), for set we can iterate through the
list and place the value in the correct location (Assuming
increasing time E.g. 0- 5s), for the get we can then use binary search to 
find the correct timestamp to get.
"""

class TimeMap:

    def __init__(self):
        self.timeMap = {}       

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        sol = ""
        values = self.timeMap.get(key, [])

        l, r = 0, (len(values) - 1)

        while l <= r:
            m = (l + r) // 2
            if timestamp >= values[m][1]:
                sol = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return sol


        
