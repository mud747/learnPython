def singleNumber(nums: list[int]) -> int:
    """
    Given an array of integers, every element appears twice except for one. Find that single one.
    """
    nums.sort()
    if len(nums) == 1:
        return nums[0]
    for i in range(0, len(nums), 2):
        # print(i)
        if i == len(nums) - 1:
            return nums[i]
        if nums[i] != nums[i+1]:
            return nums[i]

print(singleNumber([4,1,2,1,2]))
print(singleNumber([2,2,1]))

