from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            sorted_s = str(sorted(s))

            if sorted_s not in hmap:
                hmap[sorted_s]= [s]
            else:
                hmap[sorted_s].append(s)

        results = [v for k, v in hmap.items()]
        
        return results
