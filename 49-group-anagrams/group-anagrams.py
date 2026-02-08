class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        for item in strs:
            key = tuple(sorted(item))
            groups[key].append(item)
        return list(groups.values())
        