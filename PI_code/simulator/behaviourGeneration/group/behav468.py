#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( dist , prey[1] )
	temp1 = prey[1] * temp0
	temp0 = min( otherHunter[1] , otherHunter[0] )
	if otherHunter[1] != 0:
		temp2 = otherHunter[1] / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp2 = prey[1] * otherHunter[1]
	if prey[1] != 0:
		temp2 = temp1 % prey[1]
	else:
		temp2 = prey[1]
	if temp1 != 0:
		temp1 = temp2 % temp1
	else:
		temp1 = temp1
	temp0 = min( otherHunter[1] , otherHunter[0] )
	return [ otherHunter[0] , otherHunter[0] ]
