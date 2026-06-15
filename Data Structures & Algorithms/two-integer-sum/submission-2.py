class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i,num in enumerate(nums):
            needed = target-num
            if needed in a:
                return [a[needed],i]

            a[num]=i

            