class Solution:
    def getAlternates(self, arr):
        L = []
        for i in range(len(arr)):
            if i%2 == 0:
                L.append(arr[i])
        return L