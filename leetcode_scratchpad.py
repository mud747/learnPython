class Solution_1:
    def rotate(self, nums: List[int], k: int) -> None:
        """Do not return anything, modify nums in-place instead.

        """
        nums.reverse()
    
        for i in range(k):
            nums.append(nums.pop(0))
        nums.reverse()

class Solution_2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given an array of integers, find if the array contains any duplicates.
        Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
        """
        return self.foo(nums)

    def foo(self, nums):
        nums_set = set(nums)
        return len(nums_set) != len(nums)

class Solution_3:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Given an array of integers, every element appears twice except for one. Find that single one.
        """
        nums.sort()
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i+1]:
                return nums[i]
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Given an array of integers, every element appears twice except for one. Find that single one.
        """
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i+1]:
                return nums[i]

    print(singleNumber([4,1,2,1,2]))
    print(singleNumber([2,2,1]))

