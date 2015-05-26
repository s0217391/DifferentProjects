#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist + prey[1]
	temp1 = prey[1] + otherHunter[0]
	if otherHunter[1] != 0:
		temp0 = prey[1] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = dist - prey[0]
	temp1 = prey[1] * otherHunter[1]
	temp2 = -1 * dist
	temp3 = -1 * dist
	temp3 = min( prey[1] , prey[1] )
	if prey[0] > prey[1] :
		if otherHunter[1] != 0:
			temp3 = temp0 % otherHunter[1]
		else:
			temp3 = otherHunter[1]
	else:
		temp3 = max( temp1 , temp3 )
	return [ dist , prey[1] ]
