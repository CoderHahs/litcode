# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# only implemented the O(n) solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_n = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            if (nums[i] + sum_n > nums[i]):
                sum_n = nums[i] + sum_n
            else:
                sum_n = nums[i]
            if(sum_n > max_sum):
                max_sum = sum_n

        return max_sum
