#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[0]
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = otherHunter[0] - prey[0]
	temp2 = dist * dist
	if temp2 != 0:
		temp0 = dist / temp2
	else:
		temp0 = temp2
	if prey[0] != 0:
		temp3 = otherHunter[0] % prey[0]
	else:
		temp3 = prey[0]
	temp4 = -1 * dist
	temp1 = min( otherHunter[0] , temp1 )
	temp3 = prey[0] * otherHunter[0]
	if prey[1] != 0:
		temp2 = otherHunter[1] / prey[1]
	else:
		temp2 = prey[1]
	if otherHunter[1] != 0:
		temp5 = dist / otherHunter[1]
	else:
		temp5 = otherHunter[1]
	return [ prey[1] , temp2 ]
