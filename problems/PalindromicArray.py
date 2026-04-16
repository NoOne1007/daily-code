class Solution:
    def isPalinArray(self, arr):
        for i in arr:
            j = str(i)
            n = len(j)
            for k in range(n//2):
                if j[k] != j[n-k-1]:
                    return False
        return True