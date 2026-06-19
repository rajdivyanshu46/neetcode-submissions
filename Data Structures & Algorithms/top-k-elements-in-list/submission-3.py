class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}

        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1

        sorted_items = sorted(a.items(), key=lambda x: x[1], reverse=True)

        res = []
        for num, count in sorted_items[:k]:
            res.append(num)

        return res