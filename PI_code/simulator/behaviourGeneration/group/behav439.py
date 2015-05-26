#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = otherHunter[0] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = prey[0] + otherHunter[0]
	temp2 = otherHunter[1] - temp0
	temp1 = otherHunter[0] + otherHunter[0]
	temp0 = min( dist , otherHunter[0] )
	temp2 = prey[0] * temp2
	temp3 = -1 * otherHunter[1]
	return [ otherHunter[0] , otherHunter[1] ]
