class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We want to return the top k frequent elements 
        freq_map = {}
        ans = []*k

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1  
            else:
                freq_map[num] = 1  


        values = list(freq_map.items())
        values.sort(key = lambda x: x[1], reverse=True)

        for x in range(k):
            ans.append(values[x][0])

        return ans

        
    
        
        
