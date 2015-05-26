#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[0]
	temp1 = prey[1] * temp0
	if dist > prey[0] :
		if prey[0] > otherHunter[1] :
			if dist != 0:
				temp1 = dist / dist
			else:
				temp1 = dist
		else:
			temp1 = temp1 * prey[1]
	else:
		temp1 = otherHunter[0] - dist
	return [ otherHunter[0] , otherHunter[1] ]
