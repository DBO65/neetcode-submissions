class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)

        for word in strs:
            key = [0]*26
            for let in word:
                key[ord(let) - ord("a")] += 1
            sol[tuple(key)].append(word)

        return list(sol.values())



        
 