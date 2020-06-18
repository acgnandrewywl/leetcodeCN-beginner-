# Solution 1
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s1 in s2*2


# Solution 2
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        if s1 == s2:
            return True

        for i in range(len(s1)):
            tmp = s1[i:] + s1[:i]
            if tmp == s2:
                return True
        return False