class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                total = nums[i] + nums[j]
                if total == target:
                    #print("Output: [{},{}]".format(i,j))
                    return [i,j]