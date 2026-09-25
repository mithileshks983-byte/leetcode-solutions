## Problem: Reverse Linked List (Easy)
**Link:** https://leetcode.com/problems/reverse-linked-list/

### Approach
Used an iterative approach with three pointers (`prev`, `curr`, and `next_temp`). As I traversed the list, I temporarily stored the next node, reversed the current node's pointer to point to the previous node, and then shifted both `prev` and `curr` one step forward. 

### Complexity
- Time: $O(n)$
- Space: $O(1)$

### Notes
This is a classic linked list manipulation problem. Doing it iteratively is $O(1)$ space, whereas a recursive approach would use $O(n)$ space due to the call stack.