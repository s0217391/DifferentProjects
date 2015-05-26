#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > prey[1] :
		if prey[1] > otherHunter[0] :
			temp0 = dist * prey[1]
		else:
			if prey[1] != 0:
				temp0 = otherHunter[1] % prey[1]
			else:
				temp0 = prey[1]
	else:
		if otherHunter[1] != 0:
			temp0 = otherHunter[0] / otherHunter[1]
		else:
			temp0 = otherHunter[1]
	temp1 = prey[1] * dist
	temp2 = -1 * temp0
	return [ prey[1] , prey[1] ]
