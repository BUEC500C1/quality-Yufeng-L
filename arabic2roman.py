#Copyright2020 Yufeng Lin yflin@bu.edu
#EC500:Assignment one
#Arabic to Roman Numerals

def toRoman(n):
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
	print(toRoman(988))
	print(toRoman(1340))
