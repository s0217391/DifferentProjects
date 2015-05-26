#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[1]
	if otherHunter[0] != 0:
		temp1 = prey[0] / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if temp0 != 0:
		temp0 = prey[0] % temp0
	else:
		temp0 = temp0
	temp2 = -1 * temp0
	return [ temp0 , temp2 ]
