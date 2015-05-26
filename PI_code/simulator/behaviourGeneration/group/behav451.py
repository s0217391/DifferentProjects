#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[0]
	temp1 = -1 * otherHunter[1]
	if temp0 != 0:
		temp2 = prey[0] % temp0
	else:
		temp2 = temp0
	if temp1 != 0:
		temp1 = otherHunter[0] % temp1
	else:
		temp1 = temp1
	temp0 = temp0 - otherHunter[1]
	return [ temp1 , prey[1] ]
