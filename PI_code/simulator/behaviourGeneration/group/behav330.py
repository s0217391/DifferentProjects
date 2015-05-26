#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * prey[1]
	temp1 = max( otherHunter[1] , prey[0] )
	temp2 = max( prey[1] , prey[0] )
	temp0 = otherHunter[1] - temp1
	temp0 = min( temp1 , temp1 )
	temp1 = max( prey[0] , temp2 )
	temp0 = max( temp0 , prey[1] )
	if temp1 != 0:
		temp0 = dist / temp1
	else:
		temp0 = temp1
	temp1 = prey[0] * temp1
	temp1 = temp2 - temp2
	if temp2 > prey[0] :
		if prey[0] > prey[0] :
			if prey[0] > temp0 :
				temp0 = -1 * otherHunter[0]
			else:
				temp0 = min( prey[1] , temp2 )
		else:
			temp0 = dist + prey[1]
	else:
		temp0 = temp0 * prey[0]
	temp1 = -1 * otherHunter[0]
	if otherHunter[1] != 0:
		temp2 = temp0 % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp1 = otherHunter[1] * prey[1]
	temp3 = min( otherHunter[0] , otherHunter[1] )
	temp1 = otherHunter[1] - otherHunter[0]
	temp1 = prey[0] + otherHunter[1]
	if temp3 != 0:
		temp3 = temp1 % temp3
	else:
		temp3 = temp3
	temp0 = -1 * otherHunter[1]
	temp2 = min( temp2 , prey[1] )
	temp2 = -1 * temp1
	temp2 = min( temp2 , prey[0] )
	return [ prey[0] , temp1 ]
