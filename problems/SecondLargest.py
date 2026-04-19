class Solution:
    def getSecondLargest(self, arr):
        try:
            unique = sorted(set(arr), reverse=True)
            return unique[1]
        except:
            return -1