#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] - prey[0]
	temp1 = -1 * otherHunter[1]
	temp2 = -1 * temp0
	temp1 = -1 * otherHunter[0]
	temp2 = -1 * otherHunter[0]
	temp3 = max( temp1 , temp2 )
	temp0 = min( temp2 , prey[0] )
	if temp3 > temp3 :
		if temp1 != 0:
			temp3 = otherHunter[1] / temp1
		else:
			temp3 = temp1
	else:
		temp3 = prey[0] + dist
	if temp1 != 0:
		temp3 = prey[0] % temp1
	else:
		temp3 = temp1
	return [ prey[1] , temp3 ]
