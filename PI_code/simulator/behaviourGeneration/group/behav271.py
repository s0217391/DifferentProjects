#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[0] , otherHunter[0] )
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	if prey[1] > otherHunter[1] :
		temp1 = -1 * dist
	else:
		if temp0 != 0:
			temp1 = dist % temp0
		else:
			temp1 = temp0
	temp2 = temp0 + otherHunter[0]
	temp1 = temp2 * otherHunter[1]
	temp1 = otherHunter[0] + temp1
	if temp0 != 0:
		temp3 = temp1 % temp0
	else:
		temp3 = temp0
	temp0 = otherHunter[0] - otherHunter[1]
	temp4 = min( temp3 , otherHunter[1] )
	temp2 = -1 * temp0
	temp3 = min( otherHunter[1] , dist )
	if temp1 != 0:
		temp1 = prey[0] / temp1
	else:
		temp1 = temp1
	temp4 = dist + dist
	temp2 = temp3 + otherHunter[0]
	temp5 = dist * dist
	temp3 = min( temp2 , temp4 )
	if otherHunter[0] != 0:
		temp6 = temp1 % otherHunter[0]
	else:
		temp6 = otherHunter[0]
	temp7 = prey[0] * temp4
	temp8 = temp7 + temp2
	if otherHunter[1] > otherHunter[0] :
		temp1 = otherHunter[1] * temp3
	else:
		temp1 = -1 * temp4
	temp4 = max( temp3 , temp1 )
	temp9 = temp8 + temp3
	return [ temp4 , temp1 ]
