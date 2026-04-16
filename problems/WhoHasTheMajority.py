import collections
class Solution:
    def moreFrequent(self, arr, x, y):
        dict_1 = collections.Counter(arr)
        if dict_1[x] == dict_1[y]:
            return (min(x, y))
        elif dict_1[x] > dict_1[y]:
            return x
        else:
            return y