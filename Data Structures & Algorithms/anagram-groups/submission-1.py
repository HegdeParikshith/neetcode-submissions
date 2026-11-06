class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramHashmap = defaultdict(list)

        for i in range(len(strs)):
            sortedKey = "".join(sorted(strs[i]))
            anagramHashmap[sortedKey].append(strs[i])
        return list(anagramHashmap.values())
        