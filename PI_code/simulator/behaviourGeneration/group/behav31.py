#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] * otherHunter[1]
	temp1 = min( temp0 , temp0 )
	temp2 = dist * prey[1]
	temp3 = -1 * dist
	temp0 = temp0 + temp1
	if prey[1] != 0:
		temp3 = otherHunter[0] / prey[1]
	else:
		temp3 = prey[1]
	if prey[0] > otherHunter[0] :
		if temp1 != 0:
			temp4 = dist % temp1
		else:
			temp4 = temp1
	else:
		temp4 = temp3 - dist
	temp3 = dist + temp4
	temp5 = temp1 * temp1
	temp5 = max( otherHunter[0] , dist )
	if temp0 != 0:
		temp3 = temp1 % temp0
	else:
		temp3 = temp0
	if temp2 > temp0 :
		if temp0 != 0:
			temp2 = temp2 % temp0
		else:
			temp2 = temp0
	else:
		temp2 = otherHunter[0] - prey[0]
	if prey[0] > prey[0] :
		if temp4 > temp4 :
			temp2 = temp5 - dist
		else:
			if temp1 > prey[1] :
				temp2 = min( dist , temp3 )
			else:
				if temp4 != 0:
					temp2 = temp0 % temp4
				else:
					temp2 = temp4
	else:
		temp2 = max( temp0 , temp1 )
	temp1 = temp3 * prey[1]
	temp0 = temp2 - temp0
	return [ temp3 , temp2 ]
