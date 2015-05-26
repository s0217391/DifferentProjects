#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] - otherHunter[0]
	temp1 = max( dist , otherHunter[0] )
	if otherHunter[1] != 0:
		temp0 = prey[0] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp2 = prey[0] * otherHunter[1]
	if temp1 != 0:
		temp1 = temp0 / temp1
	else:
		temp1 = temp1
	temp3 = -1 * otherHunter[0]
	return [ temp0 , temp0 ]
