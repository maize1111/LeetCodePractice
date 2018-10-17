# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, last = 1, n
        while first < last:
            guess = int((first + last) / 2)
            if not isBadVersion(guess):
                first = guess+1
            else:
                last = guess
        return last
