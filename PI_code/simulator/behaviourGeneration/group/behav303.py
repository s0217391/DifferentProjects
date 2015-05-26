#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , prey[0] )
	temp1 = min( dist , temp0 )
	if prey[1] != 0:
		temp0 = temp1 / prey[1]
	else:
		temp0 = prey[1]
	temp2 = max( temp1 , temp1 )
	if otherHunter[1] != 0:
		temp1 = temp0 % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if otherHunter[0] != 0:
		temp0 = otherHunter[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp3 = min( prey[1] , prey[0] )
	temp2 = -1 * temp1
	temp0 = temp3 + temp3
	temp3 = dist * temp0
	temp2 = prey[0] * prey[0]
	temp4 = min( temp0 , otherHunter[1] )
	if otherHunter[1] != 0:
		temp2 = dist % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp5 = max( temp0 , otherHunter[1] )
	temp3 = max( temp2 , otherHunter[0] )
	temp6 = -1 * temp4
	temp3 = temp2 * temp3
	temp3 = temp6 + temp2
	temp6 = max( prey[0] , temp1 )
	if temp1 != 0:
		temp3 = temp3 / temp1
	else:
		temp3 = temp1
	temp7 = max( temp0 , otherHunter[1] )
	if prey[0] != 0:
		temp5 = otherHunter[1] % prey[0]
	else:
		temp5 = prey[0]
	temp8 = temp5 + temp2
	if temp5 != 0:
		temp8 = temp1 % temp5
	else:
		temp8 = temp5
	temp3 = otherHunter[1] - temp2
	return [ temp5 , temp4 ]
