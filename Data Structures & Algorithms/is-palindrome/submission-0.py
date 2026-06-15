class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        b = s.lower()
        for char in b:
            if char.isalnum():
                a+=char
        t = a[::-1]
        if a==t:
            return True
        return False
        