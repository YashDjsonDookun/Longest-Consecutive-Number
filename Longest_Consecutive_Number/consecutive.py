'''
	This problem was recently asked by Amazon:
	You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.

	For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.

	def longest_consecutive(nums):
	  # Fill this in.

	print longest_consecutive([100, 4, 200, 1, 3, 2])
	# should output: 4 <--
'''
class Consecutive:
	def longest_consecutive(self, nums):
		consecutiveNums = 1
		largest = 1 # My assumption is that a unique number is a longest consecutive sequence in itself
		# BubbleSort the array in ASC order
		for i in range (len(nums)):
			for j in range (len(nums) -1):
				if (nums[j] > nums[j+1]):
					nums[j], nums[j+1] = nums[j+1], nums[j]
		# Checks if next number is indeed an exact increment of one
		for i in range (len(nums) -1):
			if (nums[i]+1 == nums[i+1]):
				consecutiveNums += 1
				if consecutiveNums > largest:
					largest = consecutiveNums
			else:
				consecutiveNums = 1
		print()
		print(nums)
		return largest

# print(Consecutive().longest_consecutive([100,4,200,1,3,2]))
# print(Consecutive().longest_consecutive([100,4,200,1,30,2]))
# print(Consecutive().longest_consecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
# print(Consecutive().longest_consecutive([9,1,4,7,3,100,0,5,8,12,6]))
