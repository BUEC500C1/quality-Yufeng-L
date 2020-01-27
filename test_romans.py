#Copyright 2020 Yufeng Lin yflin@bu.edu
#test romans convertor

import pytest
import arabic2roman


def testset1():

	arabic = [3,6,18,101,-1,0,3999,1340,4001]
	correct_ans =["III","VI","XVIII","CI",-1,-1,-1,"MCCCXL",-1]
	for a,c in zip(arabic,correct_ans):
		assert arabic2roman.toRoman(a) == c


def testset2():
	assert arabic2roman.toRoman(1) == "I"
	assert arabic2roman.toRoman(2) == "II"
	assert arabic2roman.toRoman(4) == "IV"
	assert arabic2roman.toRoman(999) == "CMXCIX"
	assert arabic2roman.toRoman(1024) == "MXXIV"
	assert arabic2roman.toRoman(-3) == -1
	assert arabic2roman.toRoman(-267) == -1
	assert arabic2roman.toRoman(6789) == -1

# if __name__ == "__main__":
# 	testans()




