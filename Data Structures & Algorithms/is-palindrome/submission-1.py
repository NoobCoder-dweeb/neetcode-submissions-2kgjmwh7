class Solution:
    def isPalindrome(self, s: str) -> bool:
        reformatted = s.lower()
        reformatted = "".join(ch for ch in reformatted if ch.isalnum())

        return reformatted == reformatted[::-1]