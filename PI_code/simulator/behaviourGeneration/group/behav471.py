#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( dist , otherHunter[1] )
	if dist != 0:
		temp1 = prey[0] % dist
	else:
		temp1 = dist
	if prey[1] != 0:
		temp1 = temp1 % prey[1]
	else:
		temp1 = prey[1]
	return [ otherHunter[1] , prey[0] ]
