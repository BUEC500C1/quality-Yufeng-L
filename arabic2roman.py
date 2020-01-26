#Copyright2020 Yufeng Lin yflin@bu.edu
#EC500:Assignment one
#Arabic to Roman Numerals


def toRoman(n):
	assert 0 < n < 3999, "Input out of range"
	assert isinstance(n,int), "Incorrect input type"
    #can't represent below 1 and above 3999
    #n should be an integer
	res = ''
	nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	romans =  ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
	
	temp = n

	for i in range(len(nums)):
		while temp >= nums[i]:
			temp -= nums[i]
			res += romans[i]
	return res

if __name__ == "__main__":
	testset = [5,18,29,1350,3999]
	for element in testset:
		print(toRoman(element))
