class Solution:
	def countOddEven(self, arr):
		odd_count = 0
		even_count = 0
		for i in arr:
			if i%2 == 0:
				even_count += 1
			else:
				odd_count += 1
		return [odd_count, even_count]