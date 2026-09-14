class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

# Local Test Cases
sol = Solution()
print("Test 1 (Typical):", sol.maxProfit([7, 1, 5, 3, 6, 4])) # Expected output: 5
print("Test 2 (No profit):", sol.maxProfit([7, 6, 4, 3, 1]))  # Expected output: 0