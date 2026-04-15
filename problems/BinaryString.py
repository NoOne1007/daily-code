class Solution:
    def binarySubstring(self, s):
        count = 0
        n = len(s)
        for i in range(n):
            if int(s[i]) == 1:
                for j in range(i+1, n):
                    if int(s[j]) == 1:
                        count += 1
        return count