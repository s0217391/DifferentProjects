#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = prey[1] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if dist > prey[0] :
		if otherHunter[0] != 0:
			temp1 = prey[1] % otherHunter[0]
		else:
			temp1 = otherHunter[0]
	else:
		temp1 = temp0 - dist
	temp0 = otherHunter[0] + otherHunter[0]
	if prey[0] != 0:
		temp0 = dist / prey[0]
	else:
		temp0 = prey[0]
	if otherHunter[1] > dist :
		temp0 = otherHunter[1] * temp0
	else:
		temp0 = max( otherHunter[0] , prey[0] )
	temp2 = -1 * otherHunter[1]
	temp3 = -1 * dist
	temp4 = min( prey[0] , temp3 )
	temp5 = temp4 * temp0
	temp4 = prey[1] - prey[0]
	return [ temp2 , temp2 ]
