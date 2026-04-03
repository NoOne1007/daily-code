import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
class Solution:
    def areAnagrams(self, s1, s2):
        dict_1 = {}
        dict_2 = {}
        if len(s1) == len(s2):
            for i in range(len(s1)):
                if s1[i] not in dict_1:
                    dict_1[s1[i]] =  1
                else:
                    dict_1[s1[i]] += 1
            
                if s2[i] not in dict_2:
                    dict_2[s2[i]] =  1
                else:
                    dict_2[s2[i]] += 1
            return (dict_1 == dict_2)
        else:
            return False




# import collections
# class Solution:
#     def areAnagrams(self, s1, s2):
#         return collections.Counter(s1) == collections.Counter(s2)


# class Solution:
#     def areAnagrams(self, s1, s2):
#        if len(s1) == len(s2):
#            for i in s1:
#                if i in s2:
#                     s2 = s2.replace(i, '', 1)
#                else:
#                     return False
#        else:
#             return False
#        return True


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    solution = Solution()
    if solution.areAnagrams(s1, s2):
        print("Anagrams")
    else:
        print("Not Anagrams")