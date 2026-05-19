class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)

        for w in strs:
            count = [0]*26
            for let in w:
                count[ord(let) - ord('a')] += 1
            sol[tuple(count)].append(w)
        return list(sol.values())
            
        
        return list(sol.values())