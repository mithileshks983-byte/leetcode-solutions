## Problem: Binary Search (Easy)
**Link:** https://leetcode.com/problems/binary-search/

### Approach
Used the standard two-pointer approach to divide the search interval in half during each iteration. By checking if the target is greater than or less than the middle element, the algorithm eliminates half of the remaining array per step until the target is found or the pointers cross.

### Complexity
- Time: $O(\log n)$
- Space: $O(1)$

### Notes
Using `left + (right - left) // 2` prevents potential integer overflow compared to `(left + right) // 2`. While Python handles arbitrarily large integers automatically, writing it this way builds a good habit for languages like C++ or Java.