class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

# Local Test Cases
solution = Solution()
print("Test 1 (Typical):", solution.search([-1, 0, 3, 5, 9, 12], 9)) # Expected output: 4
print("Test 2 (Edge - Target not found):", solution.search([-1, 0, 3, 5, 9, 12], 2)) # Expected output: -1
print("Test 3 (Edge - Single element):", solution.search([5], 5)) # Expected output: 0