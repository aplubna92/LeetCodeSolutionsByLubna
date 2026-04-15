class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums.sort()
        # nums=set(nums)
        # result =[]
        # for i in range(1,len(nums)+1):
        #     if i not in nums:
        #         result.append(i)
        # return result

        s = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in s]