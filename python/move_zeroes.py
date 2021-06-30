# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroesInPlace(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:

                # here count is incremented
                nums[count] = nums[i]
                count+=1

        while count < len(nums):
            nums[count] = 0
            count += 1

    def moveZeroes(self, nums: List[int]) -> List[int]:
            num_zeroes = 0
            for i in range(len(nums)-1):
                # print("start",len(nums), num_zeroes, nums)
                if (i-1 == len(nums) - num_zeroes):
                    break
                if(nums[i] == 0):
                    num_zeroes += 1
                    # print(i, nums[:i], nums[i+1:])
                    nums = nums[:i] + nums[i+1:] + [0]
                    # print(nums)
            return nums
