## Problem: Valid Parentheses (Easy)
**Link:** https://leetcode.com/problems/valid-parentheses/

### Approach
Used a stack data structure to keep track of opening brackets. I iterated through the string, pushing opening brackets onto the stack. When a closing bracket is encountered, I popped the top element from the stack and checked if it matches the corresponding opening bracket using a hash map. If the stack is empty when trying to pop, or if the brackets don't match, the string is invalid. At the end, the stack must be empty for the string to be completely valid.

### Complexity
- Time: $O(n)$
- Space: $O(n)$

### Notes
Using a dictionary (`mapping`) makes it very easy to add new types of brackets in the future without adding a long chain of `if/else` statements.