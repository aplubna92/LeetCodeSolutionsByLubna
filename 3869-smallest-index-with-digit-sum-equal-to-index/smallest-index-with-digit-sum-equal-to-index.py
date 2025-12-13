class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for position,number in enumerate(nums):
            digit_sum = 0
            for d in str(number):
                digit_sum += int(d)
            if digit_sum == position:
                return position
        return -1

        