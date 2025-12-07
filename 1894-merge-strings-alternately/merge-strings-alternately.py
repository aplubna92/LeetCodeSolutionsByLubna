class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge = ""
        min_length = min(len(word1),len(word2))
        for i in range(min_length):
            merge += word1[i] + word2[i]
        merge += word1[min_length:] + word2[min_length:]
        return merge