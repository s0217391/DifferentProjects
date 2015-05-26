#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = otherHunter[1] / prey[1]
	else:
		temp0 = prey[1]
	if otherHunter[1] != 0:
		temp1 = dist / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp2 = -1 * temp1
	temp1 = prey[1] * otherHunter[0]
	temp2 = -1 * temp2
	temp3 = temp0 * dist
	if dist != 0:
		temp0 = prey[0] % dist
	else:
		temp0 = dist
	return [ temp0 , temp1 ]
