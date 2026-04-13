#User function Template for python3

class Solution:
    def lastIndex(self, s: str) -> int:
        last_index = -1
        for i in range(len(s)):
            if int(s[i]) == 1:
                last_index = i
        return last_index