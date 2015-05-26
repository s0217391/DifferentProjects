#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = otherHunter[1] % dist
	else:
		temp0 = dist
	if otherHunter[0] != 0:
		temp1 = otherHunter[0] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp1 = max( temp1 , prey[1] )
	temp1 = prey[0] - prey[1]
	temp0 = prey[1] * otherHunter[0]
	temp0 = min( prey[1] , prey[1] )
	return [ otherHunter[1] , otherHunter[1] ]
