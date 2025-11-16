class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vow = 0
        con = 0
        for i in s:
            if i in "aeiou":
                vow = max(vow,s.count(i))
            else:
                con = max(con,s.count(i))
        return vow+con
            
                