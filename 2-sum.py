#!/usr/bin/python3
"""representing a class Solution"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_with_index = [(nums, index) for index, num in enumerate(nums)]

        nums_with_index.sort()

        left, right= 0, len(nums) - 1

        while left < right:
            nums_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if nums_sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif nums_sum < target:
                left += 1
            else:
                right -= 1
        return 0
