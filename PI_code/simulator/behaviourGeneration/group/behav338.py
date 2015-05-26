#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > prey[1] :
		temp0 = min( dist , prey[1] )
	else:
		temp0 = otherHunter[1] + prey[0]
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp1 = max( temp1 , otherHunter[1] )
	temp0 = otherHunter[0] * temp0
	temp2 = prey[0] - otherHunter[1]
	temp3 = -1 * prey[0]
	temp1 = otherHunter[1] - prey[1]
	return [ temp1 , temp1 ]
