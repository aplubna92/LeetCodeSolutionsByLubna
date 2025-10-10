class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         total = numbers[i] + numbers[j]
        #         if total == target:
        #             return [i+1,j+1]
        start = 0
        length = len(numbers)
        while True:
            total = numbers[start] + numbers[length-1]
            if total == target:
                return [start+1,length]
            else:
                if total > target:
                    length -= 1
                else:
                    start += 1
           




        