#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + dist
	temp1 = otherHunter[1] + prey[0]
	temp2 = otherHunter[1] - dist
	temp3 = -1 * dist
	temp3 = temp0 - temp3
	if temp3 != 0:
		temp3 = otherHunter[0] / temp3
	else:
		temp3 = temp3
	temp3 = max( prey[0] , temp0 )
	temp0 = min( dist , temp1 )
	return [ dist , dist ]
