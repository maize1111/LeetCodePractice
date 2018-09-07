import operator
class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        i, A, B = 0, 0, 0
        digits = [0] * 10
        for i in range(0, len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                digits[int(secret[i])] += 1
                if digits[int(secret[i])] <= 0:
                    B += 1
                digits[int(guess[i])] -= 1
                if digits[int(guess[i])] >= 0:
                    B += 1
        return str(A) + 'A' + str(B) + 'B'
    def getHintFastest(self,secret,guess):
        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return '{}A{}B'.format(bulls,both - bulls)


test = Solution()
print(test.getHint('1870','7810'))
print(test.getHintFastest('1870','7810'))