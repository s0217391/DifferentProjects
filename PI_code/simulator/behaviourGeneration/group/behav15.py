#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = prey[1] % dist
	else:
		temp0 = dist
	if prey[1] != 0:
		temp1 = otherHunter[0] % prey[1]
	else:
		temp1 = prey[1]
	temp2 = prey[1] - temp1
	if dist != 0:
		temp3 = prey[1] / dist
	else:
		temp3 = dist
	temp3 = temp3 - prey[0]
	return [ temp3 , temp0 ]
