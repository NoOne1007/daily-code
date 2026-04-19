class Solution:
    def missingNum(self, arr):
        L = list(range(1, len(arr)+2))
        for i in L:
            if i not in arr:
                return i