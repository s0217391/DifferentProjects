#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + prey[0]
	temp1 = prey[1] - temp0
	temp1 = max( dist , prey[1] )
	temp0 = -1 * temp1
	temp0 = max( dist , prey[1] )
	temp2 = otherHunter[1] * prey[1]
	temp3 = -1 * prey[0]
	temp2 = max( otherHunter[1] , dist )
	if dist > temp1 :
		temp2 = -1 * temp0
	else:
		if temp3 != 0:
			temp2 = prey[1] / temp3
		else:
			temp2 = temp3
	temp3 = min( prey[0] , temp0 )
	return [ prey[0] , temp0 ]
