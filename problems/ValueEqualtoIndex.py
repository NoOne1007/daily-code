class Solution:
    def valueEqualToIndex(self, arr):
        L = []
        for i in range(1, len(arr) + 1):
            if i == arr[i-1]:
              L.append(i)
        return L