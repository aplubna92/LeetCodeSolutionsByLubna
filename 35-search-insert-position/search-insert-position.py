class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        length = len(nums) - 1
        while start<=length:
            midValue = (start + length) // 2
            if target == nums[midValue]:
                return midValue
            elif target < nums[midValue]:
                length = midValue -1
            else:
                start = midValue + 1
        return start