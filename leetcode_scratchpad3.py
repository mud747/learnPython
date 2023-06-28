def TwoSum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
    
# test cases
print(TwoSum([2,7,11,15], 9))
print(TwoSum([3,2,4], 6))
print(TwoSum([3,3], 6))

