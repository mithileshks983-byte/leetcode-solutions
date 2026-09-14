def twoSum(nums, target):
    prevMap = {} # val : index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return []

# Local Test Cases
print("Test 1 (Typical):", twoSum([2, 7, 11, 15], 9)) # Expected output: [0, 1]
print("Test 2 (Edge):", twoSum([3, 3], 6))            # Expected output: [0, 1]