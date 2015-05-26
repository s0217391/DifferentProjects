#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > prey[0] :
		temp0 = prey[0] + prey[1]
	else:
		temp0 = prey[1] - dist
	temp1 = -1 * otherHunter[1]
	if temp0 != 0:
		temp2 = otherHunter[1] / temp0
	else:
		temp2 = temp0
	if temp2 != 0:
		temp1 = temp1 % temp2
	else:
		temp1 = temp2
	temp1 = -1 * otherHunter[1]
	if otherHunter[1] > prey[1] :
		temp3 = min( otherHunter[0] , prey[1] )
	else:
		if prey[0] != 0:
			temp3 = temp1 / prey[0]
		else:
			temp3 = prey[0]
	return [ prey[1] , prey[1] ]
