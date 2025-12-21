class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        freq = {}
        mx = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            mx = max(mx, right - left + 1)
        return mx