class Solution:
    def removeSpaces(self, s):
        L = []
        for i in s:
            if i == " ":
                pass
            else:
                L.append(i)
        return "".join(L)