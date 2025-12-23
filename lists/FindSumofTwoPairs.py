# Find the sum of two pairs that equal to the given value
def FindSumofPairs(nums: list, target: int) -> int:
    for j in range(len(nums)): # O(n)
        for i in range(j+1, len(nums)): # O(n) ----- O(n^2)
            if nums[j] == nums[i]:
                continue
            elif nums[j] + nums[i] == target:
                print(nums[j], nums[i])

print(FindSumofPairs([2,5,6,3,5,3,5,2,5,3,5,3], 8))
