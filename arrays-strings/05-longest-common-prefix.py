class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while s.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

# Local Test Cases
sol = Solution()
print("Test 1 (Typical):", sol.longestCommonPrefix(["flower","flow","flight"])) # Expected: "fl"
print("Test 2 (No prefix):", sol.longestCommonPrefix(["dog","racecar","car"]))    # Expected: ""