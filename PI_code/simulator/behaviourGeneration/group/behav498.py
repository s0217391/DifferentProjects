#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	temp1 = otherHunter[1] * prey[0]
	temp2 = temp0 * dist
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	temp2 = temp1 * prey[0]
	temp1 = dist + temp0
	if temp0 != 0:
		temp2 = prey[1] % temp0
	else:
		temp2 = temp0
	temp3 = otherHunter[1] * dist
	if otherHunter[1] != 0:
		temp4 = otherHunter[0] / otherHunter[1]
	else:
		temp4 = otherHunter[1]
	return [ prey[1] , temp4 ]
