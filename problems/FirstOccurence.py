class Solution:
    def firstOccurence(self,txt,pat):
        n = len(txt)
        m = len(pat)

        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if txt[i + j] != pat[j]:
                    match = False
                    break
            if match:
                return i

        return -1