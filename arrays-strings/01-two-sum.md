## Problem: Two Sum (Easy)
**Link:** https://leetcode.com/problems/two-sum/

### Approach
I used a hash map to store previously seen numbers and their indices. For each number, I calculate the difference needed to reach the target and check if that difference already exists in the map.

### Complexity
- Time: $O(N)$
- Space: $O(N)$

### Notes
Using a hash map allows for a single pass through the array, which is much more efficient than using nested loops.