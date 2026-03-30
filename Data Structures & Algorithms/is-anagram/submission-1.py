from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # cnt1 = {k: 0 for k in s}
        # cnt2 = {k: 0 for k in t}
        
        # for c in s:
        #     cnt1[c] +=1
        # for c in t:
        #     cnt2[c] +=1

        # return cnt1 == cnt2
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)
