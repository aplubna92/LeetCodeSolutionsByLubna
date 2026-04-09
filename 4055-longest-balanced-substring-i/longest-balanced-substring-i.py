class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        
        max_len = 0
        for i in range(n):
            char_dict={}
            for j in range(i,n):
                ch=s[j]
                char_dict[ch]=char_dict.get(ch,0)+1
                if len(set(char_dict.values()))==1:
                    max_len = max(max_len, j - i + 1)
        return max_len