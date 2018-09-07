class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        s1 = version1.split('.')
        # print(s1)
        s2 = version2.split('.')
        # print(s2)

        length1 = len(s1)
        length2 = len(s2)
        maxLen = max(length1, length2)

        for i in range(maxLen):
            temp1, temp2 = 0, 0
            if i < length1:
                temp1 = int(s1[i])
            if i < length2:
                temp2 = int(s2[i])
            if temp1 > temp2:
                return 1
            elif temp1 < temp2:
                return -1
        return 0


test = Solution()
print(test.compareVersion("1.0", "1"))
