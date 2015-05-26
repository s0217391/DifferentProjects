#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = otherHunter[1] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * dist
	if prey[0] != 0:
		temp2 = otherHunter[0] % prey[0]
	else:
		temp2 = prey[0]
	temp0 = prey[1] - prey[1]
	temp1 = temp2 * prey[1]
	temp3 = temp0 + otherHunter[0]
	if temp0 > temp2 :
		temp0 = prey[0] + otherHunter[0]
	else:
		temp0 = -1 * temp3
	return [ dist , temp3 ]
