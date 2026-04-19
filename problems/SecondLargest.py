class Solution:
    def getSecondLargest(self, arr):
        largest = float('-inf')
        second_largest = float('-inf')
        for i in arr:
            if i > largest:
                second_largest, largest = largest, i
            elif largest > i > second_largest:
                second_largest = i
        if second_largest > float('-inf'):
            return second_largest
        else:
            return -1
            
            
        # try:
        #     unique = sorted(set(arr), reverse=True)
        #     return unique[1]
        # except IndexError:
        #     return -1