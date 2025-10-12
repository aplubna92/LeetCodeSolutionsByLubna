class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = "".join([k.lower() for k in s if k.isalnum()])
        # s2 = s1[::-1]
        return s1 == s1[::-1]
        #     return True
        # else:
        #     return False
