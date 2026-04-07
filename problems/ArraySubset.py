#User function Template for python3
import collections
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        d1 = collections.Counter(a)
        d2 = collections.Counter(b)
        for x in d2.keys():
            if x in d1:
                if d2[x] > d1[x]:
                    return False
            else:
                return False
        return True



### Solution below is not optimized

# class Solution:
#     #Function to check if a is a subset of b.
#     def isSubset(self, a, b):
#         for i in b:
#             if i in a:
#                 a.remove(i)
#             else:
#                 return False
#         return True