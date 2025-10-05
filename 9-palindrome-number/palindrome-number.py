class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1 = str(x)[::-1]
        flag = False
        if str(x) == x1:
            flag = True
        return flag
        