# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums) == 0):
            return -1
        elif (len(nums) == 1):
            return 0 if nums[0] == target else -1
        def find_pivot(arr, low, high):
            # base cases
            if high < low:
                return -1
            if high == low:
                return low

            #low + (high - low)/2;
            mid = int((low + high)/2)

            if mid < high and arr[mid] > arr[mid + 1]:
                return mid
            if mid > low and arr[mid] < arr[mid - 1]:
                return (mid-1)
            if arr[low] >= arr[mid]:
                return find_pivot(arr, low, mid-1)
            return find_pivot(arr, mid + 1, high)

        pivot = find_pivot(nums, 0, len(nums)-1)
        print(pivot)

        def binary_search (arr, l, r, x):
            if r >= l:
                mid = l + (r - l)//2
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    return binary_search(arr, l, mid-1, x)
                else:
                    return binary_search(arr, mid+1, r, x)
            else:
                return -1

        if nums[pivot] == target:
            return pivot
        if nums[0] <= target:
            return binary_search(nums, 0, pivot-1, target)
        return binary_search(nums, pivot+1, len(nums)-1, target)
