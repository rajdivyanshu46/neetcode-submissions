class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        for char in s:
            if char not in a:
                a[char] = 1
            else:
                a[char]+=1
        for char in t:
            if char not in b:
                b[char] = 1
            else:
                b[char]+=1
        if a==b:
            return True
        else:
            return False