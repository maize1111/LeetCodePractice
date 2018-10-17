class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9


test = Solution()
print(test.addDigits(38))
