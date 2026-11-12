class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # option 1: using for loop
        # ===================================
        # for letter in letters:
        #     if letter > target:
        #         return letter
        # return letters[0]

        # option 2: using binary search method
        left =0
        right = len(letters)-1

        while (left<=right):
            mid = (left + right) // 2

            if letters[mid] <= target :
                left = mid +1
            else:
                right = mid - 1
        if left == len(letters):
            return letters[0]
        return letters[left]