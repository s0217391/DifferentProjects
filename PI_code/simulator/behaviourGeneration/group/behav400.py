#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = temp0 + otherHunter[0]
	temp0 = temp0 - dist
	return [ prey[1] , temp1 ]
