class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups  = {}
        for words in strs:
            key = [0] * 26
            for c in words:
                key[ord(c) - ord('a')] += 1

            key = tuple(key)
            if key not in groups:
                groups[key] = []
            groups[key].append(words)
        
        return list(groups.values())
    