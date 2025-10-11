class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in nums:
            for d in str(i):
                total += int(d)
        return sum(nums) - total

        