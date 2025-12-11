class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = " ".join(word[::-1] for word in s.split())
        return result
        