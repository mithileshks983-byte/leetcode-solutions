## Problem: Longest Common Prefix (Easy)
**Link:** https://leetcode.com/problems/longest-common-prefix/

### Approach
I used horizontal scanning. I take the first string as the initial prefix and compare it with the next string, shortening the prefix from the end until it matches the beginning of the string. I repeat this for all strings.

### Complexity
- Time: $O(S)$ where S is the sum of all characters in all strings
- Space: $O(1)$

### Notes
Shortening the prefix using slicing is an efficient way to find the common starting characters without needing complex nested loops.