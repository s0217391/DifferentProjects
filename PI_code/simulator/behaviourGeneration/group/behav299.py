#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = otherHunter[0] / prey[0]
	else:
		temp0 = prey[0]
	if otherHunter[1] > prey[1] :
		if temp0 != 0:
			temp1 = temp0 / temp0
		else:
			temp1 = temp0
	else:
		temp1 = min( otherHunter[1] , prey[0] )
	if temp1 != 0:
		temp1 = prey[1] % temp1
	else:
		temp1 = temp1
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp2 = min( prey[1] , prey[1] )
	temp0 = otherHunter[0] + temp2
	temp3 = prey[1] - prey[1]
	return [ prey[0] , temp0 ]
