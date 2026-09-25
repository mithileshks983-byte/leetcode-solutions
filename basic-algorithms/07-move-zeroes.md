## Problem: Move Zeroes (Easy)
**Link:** https://leetcode.com/problems/move-zeroes/

### Approach
Used a two-pointer approach to track the insertion position for non-zero elements. As the loop iterates through the array, any non-zero element is swapped with the element at the `insert_pos` pointer, and `insert_pos` is incremented. This shifts all zeroes to the end while maintaining the relative order of non-zero elements.

### Complexity
- Time: $O(n)$
- Space: $O(1)$

### Notes
Swapping elements directly fulfills the problem's strict constraint to modify the array in-place without making a copy, which is more space-efficient than creating a new array.