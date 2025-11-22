class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        s = set(arr)
        cnt = 0
        for i in range(1, max(s)):
            if i not in s:
                cnt += 1
                if cnt == k:
                    return i
        return max(s) + k - cnt 