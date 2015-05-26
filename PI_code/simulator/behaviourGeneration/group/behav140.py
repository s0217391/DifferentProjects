#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = otherHunter[1] % dist
	else:
		temp0 = dist
	if otherHunter[1] != 0:
		temp1 = dist % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp1 = -1 * temp0
	return [ prey[1] , otherHunter[0] ]
