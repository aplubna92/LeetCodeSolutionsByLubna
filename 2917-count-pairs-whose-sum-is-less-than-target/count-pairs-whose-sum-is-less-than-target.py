class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right =0, len(nums)-1
        count = 0
        nums.sort()
        while left < right:
            if nums[left] + nums[right] < target:
                count += (right - left)
                left += 1
            else:
                right -= 1
        return count