#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] + prey[1]
	temp1 = max( otherHunter[1] , prey[1] )
	temp1 = otherHunter[0] + prey[0]
	if otherHunter[0] != 0:
		temp2 = otherHunter[0] % otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp3 = -1 * temp0
	return [ otherHunter[1] , prey[1] ]
