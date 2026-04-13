#User function Template for python3

import collections
class Solution:
    def firstRep(self, s):
        my_set = set()
        my_dict = collections.Counter(s)
        for i in my_dict.keys():
            if my_dict[i] > 1:
                my_set.add(i)
        
        for i in s:
            if i in my_set:
                return i
        return '#'