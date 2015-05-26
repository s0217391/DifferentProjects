#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * dist
	temp1 = prey[0] + prey[1]
	if temp0 != 0:
		temp0 = prey[0] % temp0
	else:
		temp0 = temp0
	return [ otherHunter[0] , temp1 ]
