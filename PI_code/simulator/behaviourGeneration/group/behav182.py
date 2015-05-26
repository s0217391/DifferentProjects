#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + prey[1]
	temp1 = prey[1] * dist
	temp0 = -1 * otherHunter[0]
	temp0 = -1 * otherHunter[0]
	temp1 = temp0 * prey[0]
	temp2 = min( otherHunter[1] , prey[1] )
	temp0 = -1 * prey[1]
	temp2 = -1 * temp1
	temp2 = otherHunter[0] - dist
	temp2 = min( otherHunter[0] , temp2 )
	if dist != 0:
		temp0 = otherHunter[1] % dist
	else:
		temp0 = dist
	if dist != 0:
		temp3 = otherHunter[1] % dist
	else:
		temp3 = dist
	temp0 = prey[0] * prey[1]
	if prey[0] != 0:
		temp0 = dist / prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[0] - temp1
	temp2 = temp0 * temp3
	return [ prey[1] , prey[0] ]
