#Copyright 2020 Yufeng Lin yflin@bu.edu
#test romans convertor

import pytest
import arabic2roman


def testans():

	arabic = [3,6,18,101,-1,0,3999,1340,4001]
	correct_ans =["III","VI","XVIII","CI",-1,-1,-1,"MCCCXL",-1]
	for a,c in zip(arabic,correct_ans):
		assert arabic2roman.toRoman(a) == c


# if __name__ == "__main__":
# 	testans()




