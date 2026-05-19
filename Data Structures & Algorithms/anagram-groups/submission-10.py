class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            words = [0]*26
            for let in word:
                words[ord(let)-ord('a')] += 1
            anagrams[tuple(words)].append(word)

        return list(anagrams.values()) 
        