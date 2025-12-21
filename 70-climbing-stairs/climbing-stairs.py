class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        data = {}
        def climb(n):
            if n <= 2:
                return n
            if n in data:
                return data[n]
            data[n] = climb(n-1)+climb(n-2)
            return data[n]
        return climb(n)
        
