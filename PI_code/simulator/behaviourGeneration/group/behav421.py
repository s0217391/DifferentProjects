#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > otherHunter[1] :
		temp0 = otherHunter[1] + dist
	else:
		temp0 = dist - otherHunter[0]
	temp1 = prey[1] * prey[0]
	temp2 = temp1 * temp1
	return [ temp0 , temp2 ]
