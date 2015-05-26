#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = otherHunter[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[1] - otherHunter[1]
	temp1 = otherHunter[1] - otherHunter[0]
	if prey[1] > otherHunter[0] :
		if prey[1] != 0:
			temp1 = otherHunter[0] % prey[1]
		else:
			temp1 = prey[1]
	else:
		temp1 = prey[0] - otherHunter[0]
	return [ dist , prey[0] ]
