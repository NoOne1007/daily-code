#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        rev_str = s[::-1]
        return rev_str# code here

if __name__ == "__main__":
    s = "Hello, World!"
    solution = Solution()
    reversed_s = solution.reverseString(s)
    print(reversed_s)