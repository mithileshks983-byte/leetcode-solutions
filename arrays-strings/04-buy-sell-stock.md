## Problem: Best Time to Buy and Sell Stock (Easy)
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Approach
I used a single pass through the array. I keep track of the lowest price seen so far and calculate the potential profit for every subsequent day, updating the maximum profit whenever a better one is found.

### Complexity
- Time: $O(N)$
- Space: $O(1)$

### Notes
This is much faster than checking every pair of days, which would take $O(N^2)$ time.