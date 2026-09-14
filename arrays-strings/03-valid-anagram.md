## Problem: Valid Anagram (Easy)
**Link:** https://leetcode.com/problems/valid-anagram/

### Approach
I used hash maps to count the frequency of each character in both strings. If the lengths differ, it returns False immediately. Otherwise, it populates the frequency maps and compares them.

### Complexity
- Time: $O(N)$
- Space: $O(N)$

### Notes
Using a hash map is $O(N)$ time, which is generally more efficient than sorting the strings first, which would take $O(N \log N)$ time.