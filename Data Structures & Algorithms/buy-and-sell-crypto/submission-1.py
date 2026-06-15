class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0
        b = [0]
        for i in range(len(prices)-1):
            c = prices[i+1:]
            d = max(c)
            a = max(a,d-prices[i])
            b.append(a)
        return max(b)
        
            

        