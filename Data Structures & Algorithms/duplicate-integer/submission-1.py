class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for i in nums:
            if i not in check:
                check[i] = 1
            else:
                check[i]+=1
                if check[i]>=2:
                    return True
        return False