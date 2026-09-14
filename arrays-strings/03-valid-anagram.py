class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        return countS == countT

# Local Test Cases
sol = Solution()
print("Test 1 (Typical):", sol.isAnagram("anagram", "nagaram")) # Expected output: True
print("Test 2 (Edge):", sol.isAnagram("rat", "car"))            # Expected output: False