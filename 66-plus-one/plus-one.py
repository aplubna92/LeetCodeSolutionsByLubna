class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        var = int("".join(map(str,digits)))
        var = var+1
        digits = [int(d) for d in str(var)]
        return digits
        