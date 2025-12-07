class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        """ solution 1: using plain recursion . taking 12ms"""
        return n if n<=1 else self.fib(n-2)+self.fib(n-1)

        """ taking 16ms time , still using recursion"""
        # starting_grid = {0:0, 1:1}
        # def fibo(n):
        #     if n in starting_grid:
        #         return starting_grid[n]
        #     starting_grid[n] = fibo(n-2) + fibo(n-1)
        #     return starting_grid[n]
        # return fibo(n)