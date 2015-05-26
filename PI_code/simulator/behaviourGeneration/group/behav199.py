#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = prey[0] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = prey[0] * temp0
	temp1 = -1 * otherHunter[0]
	if dist != 0:
		temp0 = dist / dist
	else:
		temp0 = dist
	return [ prey[1] , otherHunter[0] ]
