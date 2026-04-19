class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        return expected_sum - actual_sum


        # L = list(range(1, len(arr)+2))
        # for i in L:
        #     if i not in arr:
        #         return i