# Return true if s is binary, else false
class Solution:
    def isBinary(self, s):
        for i in s:
            if int(i) != 0 and int(i) != 1:
                return False
        return True