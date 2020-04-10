'''
	This problem was recently asked by Amazon:
	You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.

	For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.

	def longest_consecutive(nums):
	  # Fill this in.

	print longest_consecutive([100, 4, 200, 1, 3, 2])
	# 4
'''


class Consecutive:
	def longest_consecutive(self, nums1):
		consecutiveNums = 1
		for i in range (len(nums1)):
			for j in range (len(nums1) -1):
				if (nums1[j] > nums1[j+1]):
					nums1[j], nums1[j+1] = nums1[j+1], nums1[j]

		for i in range (len(nums1) -1):
			if (nums1[i]+1 == nums1[i+1]):
				consecutiveNums = consecutiveNums + 1
		return consecutiveNums
print(Consecutive().longest_consecutive([100,4,200,1,3,2]))