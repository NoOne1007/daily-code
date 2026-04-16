class Solution:
    def leftRotate(self, arr, d):
        L = []
        for i in range(d, len(arr)):
            L.append(arr[i])
        for j in range(d):
            L.append(arr[j])
        return L