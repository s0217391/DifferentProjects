#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	if otherHunter[1] > temp0 :
		temp1 = temp0 * prey[0]
	else:
		temp1 = otherHunter[1] - dist
	temp2 = min( otherHunter[0] , temp1 )
	temp3 = -1 * temp1
	temp1 = dist * prey[1]
	temp1 = max( prey[1] , temp2 )
	if otherHunter[0] != 0:
		temp0 = temp2 % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if prey[1] > temp2 :
		temp1 = otherHunter[1] - temp0
	else:
		if otherHunter[1] != 0:
			temp1 = dist / otherHunter[1]
		else:
			temp1 = otherHunter[1]
	if otherHunter[1] != 0:
		temp0 = prey[0] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	return [ dist , temp1 ]
