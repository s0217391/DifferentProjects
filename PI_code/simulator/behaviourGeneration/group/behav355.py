#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] + otherHunter[1]
	temp1 = prey[1] * otherHunter[1]
	temp2 = dist * otherHunter[1]
	if temp0 != 0:
		temp0 = dist % temp0
	else:
		temp0 = temp0
	if prey[1] != 0:
		temp1 = dist % prey[1]
	else:
		temp1 = prey[1]
	temp0 = otherHunter[1] * dist
	if otherHunter[0] != 0:
		temp2 = prey[0] / otherHunter[0]
	else:
		temp2 = otherHunter[0]
	return [ prey[0] , prey[1] ]
