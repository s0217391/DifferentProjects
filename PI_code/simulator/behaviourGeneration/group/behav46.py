#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[1] , prey[0] )
	temp1 = prey[0] * prey[1]
	temp1 = temp0 - temp0
	temp2 = prey[1] + dist
	if prey[0] != 0:
		temp1 = temp1 % prey[0]
	else:
		temp1 = prey[0]
	temp1 = min( temp0 , temp1 )
	if dist > temp2 :
		temp2 = -1 * temp0
	else:
		temp2 = otherHunter[1] + dist
	temp3 = temp2 - prey[0]
	temp3 = otherHunter[0] + temp0
	return [ prey[1] , prey[0] ]
