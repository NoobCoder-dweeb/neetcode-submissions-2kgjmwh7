class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        if len(strs) == 1:
            return [strs[:]]

        for s in strs:
            sorted_s = str(sorted(s))

            if sorted_s not in anagrams:
                anagrams[sorted_s]=[]

            anagrams[sorted_s].append(s)

        group_anagrams = [vals[:] for _, vals in anagrams.items()]

        return group_anagrams