#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] + prey[0]
	temp1 = -1 * dist
	temp0 = max( prey[1] , prey[1] )
	if temp0 > otherHunter[0] :
		if temp0 != 0:
			temp2 = prey[0] / temp0
		else:
			temp2 = temp0
	else:
		if otherHunter[1] != 0:
			temp2 = otherHunter[1] / otherHunter[1]
		else:
			temp2 = otherHunter[1]
	temp0 = -1 * dist
	temp1 = -1 * temp2
	temp3 = max( dist , prey[1] )
	if prey[0] > otherHunter[0] :
		temp1 = max( otherHunter[1] , prey[1] )
	else:
		temp1 = min( temp0 , otherHunter[1] )
	return [ otherHunter[0] , temp3 ]
