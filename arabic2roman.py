#Copyright2020 Yufeng Lin yflin@bu.edu
#EC500:Assignment one
#Arabic to Roman Numerals


def toRoman(n):
    #can't represent integer below 1 and above 3999
	res = ''
	nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	romans =  ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]	
	temp = n
	if 0 < temp < 3999 and isinstance(temp,int):
		for i in range(len(nums)):
		    while temp >= nums[i]:
			    temp -= nums[i]
			    res += romans[i]
		return res
	else:
	    return -1
if __name__ == "__main__":
	pass