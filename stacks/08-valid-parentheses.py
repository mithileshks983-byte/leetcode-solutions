class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack

# Local Test Cases
solution = Solution()
print("Test 1 (Typical):", solution.isValid("()[]{}")) # Expected output: True
print("Test 2 (Edge - Mismatched):", solution.isValid("(]")) # Expected output: False
print("Test 3 (Edge - Unmatched open):", solution.isValid("[")) # Expected output: False