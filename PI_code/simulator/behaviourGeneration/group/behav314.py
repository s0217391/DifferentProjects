#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * dist
	temp1 = otherHunter[0] - otherHunter[0]
	if prey[0] != 0:
		temp1 = otherHunter[1] / prey[0]
	else:
		temp1 = prey[0]
	temp1 = prey[1] - prey[1]
	temp0 = max( temp0 , prey[0] )
	temp0 = max( temp1 , temp1 )
	if temp1 > prey[0] :
		if temp0 > dist :
			temp2 = prey[1] + otherHunter[1]
		else:
			temp2 = min( otherHunter[1] , prey[0] )
	else:
		temp2 = dist - temp1
	if temp0 != 0:
		temp2 = dist / temp0
	else:
		temp2 = temp0
	if prey[0] != 0:
		temp1 = dist / prey[0]
	else:
		temp1 = prey[0]
	temp2 = -1 * otherHunter[0]
	temp2 = otherHunter[1] - otherHunter[0]
	temp3 = otherHunter[0] * otherHunter[1]
	temp4 = -1 * temp2
	temp5 = min( otherHunter[1] , otherHunter[1] )
	temp5 = prey[0] - temp3
	return [ temp0 , temp0 ]
