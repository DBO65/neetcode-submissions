class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)

        for w in strs:
            key = ''.join(sorted(w))
            sol[key].append(w)
        
        return list(sol.values())