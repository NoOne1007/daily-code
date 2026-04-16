# class Solution:
#     def search(self, arr, x):
#         for i in range(len(arr)):
#             if arr[i] == x:
#                 return i
#         return -1
    


from typing import List

class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i] == k:
                return i+1
        return -1