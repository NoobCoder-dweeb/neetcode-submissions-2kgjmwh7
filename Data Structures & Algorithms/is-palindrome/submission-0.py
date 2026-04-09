class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower()
        reformatted = "".join([ch for ch in text if ch.isalnum()])

        left = 0
        right = len(reformatted) - 1

        while left < right:
            if reformatted[left] != reformatted[right]:
                return False
            
            left += 1
            right -= 1 

        return True
        