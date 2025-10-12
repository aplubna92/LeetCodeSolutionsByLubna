class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {"{":"}","(":")","[":"]"}
        starting_brackets = ['{','[','(']
        stack = []
        for br in s:
            if br in starting_brackets:
                stack.append(br)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if br != brackets[top]:
                    return False
                stack.pop()
        return not stack


