class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Local Test Cases
sol = Solution()

test1 = ["h","e","l","l","o"]
sol.reverseString(test1)
print("Test 1 (Typical):", test1) # Expected output: ['o', 'l', 'l', 'e', 'h']

test2 = ["H","a","n","n","a","h"]
sol.reverseString(test2)
print("Test 2 (Even length):", test2) # Expected output: ['h', 'a', 'n', 'n', 'a', 'H']