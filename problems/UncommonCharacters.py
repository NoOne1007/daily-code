#User function Template for python3

import collections

class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        dict_1 = collections.Counter(s1)
        dict_2 = collections.Counter(s2)
        uncommon = set()
        for i in dict_1.keys():
            if i not in dict_2:
                uncommon.add(i)
                
        for i in dict_2.keys():
            if i not in dict_1:
                uncommon.add(i)
        
        uncommon = sorted(uncommon)
        return "".join(uncommon)