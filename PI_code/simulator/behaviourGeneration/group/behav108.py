#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = prey[1] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = otherHunter[1] - dist
	temp2 = -1 * otherHunter[0]
	if temp0 != 0:
		temp0 = otherHunter[0] / temp0
	else:
		temp0 = temp0
	temp0 = prey[1] - prey[1]
	if dist > otherHunter[0] :
		temp1 = temp2 * temp1
	else:
		if prey[1] != 0:
			temp1 = dist % prey[1]
		else:
			temp1 = prey[1]
	temp3 = -1 * temp2
	if dist != 0:
		temp3 = temp2 % dist
	else:
		temp3 = dist
	return [ otherHunter[1] , temp0 ]
