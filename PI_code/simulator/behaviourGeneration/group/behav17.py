#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , otherHunter[1] )
	temp1 = otherHunter[0] * prey[0]
	if temp0 != 0:
		temp0 = prey[1] % temp0
	else:
		temp0 = temp0
	if prey[0] > dist :
		temp2 = temp0 * otherHunter[0]
	else:
		temp2 = min( dist , otherHunter[0] )
	temp0 = -1 * temp1
	temp2 = prey[0] * otherHunter[0]
	if temp1 != 0:
		temp2 = temp2 % temp1
	else:
		temp2 = temp1
	if dist > prey[0] :
		temp1 = dist - otherHunter[1]
	else:
		if otherHunter[0] != 0:
			temp1 = temp2 / otherHunter[0]
		else:
			temp1 = otherHunter[0]
	if prey[1] != 0:
		temp3 = prey[0] / prey[1]
	else:
		temp3 = prey[1]
	temp0 = temp1 + temp3
	if temp0 != 0:
		temp4 = prey[1] % temp0
	else:
		temp4 = temp0
	return [ temp0 , prey[1] ]
