class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1

# Local Test Cases
solution = Solution()

arr1 = [0, 1, 0, 3, 12]
solution.moveZeroes(arr1)
print("Test 1 (Typical):", arr1) # Expected output: [1, 3, 12, 0, 0]

arr2 = [0]
solution.moveZeroes(arr2)
print("Test 2 (Edge - Single zero):", arr2) # Expected output: [0]

arr3 = [2, 1]
solution.moveZeroes(arr3)
print("Test 3 (Edge - No zeroes):", arr3) # Expected output: [2, 1]