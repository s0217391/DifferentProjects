#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] - otherHunter[0]
	temp1 = max( otherHunter[0] , temp0 )
	temp2 = otherHunter[1] + otherHunter[1]
	temp2 = -1 * prey[1]
	temp3 = otherHunter[1] * otherHunter[1]
	temp0 = temp1 * prey[0]
	temp0 = temp0 * temp1
	temp4 = otherHunter[0] * prey[0]
	temp2 = min( temp3 , prey[0] )
	temp5 = -1 * otherHunter[0]
	if prey[0] != 0:
		temp2 = otherHunter[0] % prey[0]
	else:
		temp2 = prey[0]
	temp3 = otherHunter[1] - temp0
	if temp3 > temp1 :
		temp1 = min( prey[1] , temp0 )
	else:
		if prey[1] > otherHunter[1] :
			if temp1 > dist :
				temp1 = temp5 * temp3
			else:
				if prey[1] > prey[1] :
					temp1 = temp1 - prey[1]
				else:
					temp1 = otherHunter[0] - temp3
		else:
			if prey[0] > temp3 :
				temp1 = temp0 + otherHunter[0]
			else:
				temp1 = min( prey[0] , temp0 )
	temp3 = prey[0] - dist
	temp4 = -1 * dist
	temp3 = dist * prey[1]
	temp6 = temp3 - otherHunter[0]
	temp7 = -1 * prey[1]
	if temp2 != 0:
		temp5 = temp3 % temp2
	else:
		temp5 = temp2
	if prey[0] != 0:
		temp6 = temp1 % prey[0]
	else:
		temp6 = prey[0]
	if temp4 != 0:
		temp0 = temp7 % temp4
	else:
		temp0 = temp4
	temp4 = min( temp2 , temp0 )
	temp1 = dist * temp5
	if temp0 > temp4 :
		temp1 = min( dist , dist )
	else:
		temp1 = temp1 * temp5
	return [ otherHunter[0] , temp6 ]
