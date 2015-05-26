#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] - otherHunter[0]
	temp1 = min( otherHunter[0] , temp0 )
	if dist > prey[1] :
		temp0 = min( dist , prey[0] )
	else:
		temp0 = otherHunter[0] + otherHunter[1]
	temp0 = temp1 * otherHunter[0]
	temp1 = prey[1] - prey[1]
	temp0 = otherHunter[1] * otherHunter[0]
	temp0 = -1 * dist
	temp1 = max( temp1 , prey[0] )
	temp0 = -1 * otherHunter[1]
	temp2 = temp1 - prey[1]
	temp1 = max( otherHunter[1] , temp2 )
	temp2 = min( otherHunter[0] , temp2 )
	temp0 = temp1 + prey[0]
	if prey[1] > prey[0] :
		temp0 = max( otherHunter[1] , otherHunter[0] )
	else:
		if prey[1] != 0:
			temp0 = prey[0] / prey[1]
		else:
			temp0 = prey[1]
	if temp1 != 0:
		temp2 = prey[0] / temp1
	else:
		temp2 = temp1
	temp2 = prey[1] + temp2
	temp0 = -1 * otherHunter[0]
	temp0 = otherHunter[1] * temp1
	temp3 = max( temp1 , prey[0] )
	temp2 = -1 * temp2
	temp4 = max( temp2 , temp3 )
	temp2 = max( temp1 , prey[1] )
	temp3 = prey[0] * prey[0]
	temp2 = max( temp0 , otherHunter[1] )
	return [ temp3 , prey[1] ]
