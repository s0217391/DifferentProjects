#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , dist )
	if temp0 != 0:
		temp1 = otherHunter[0] % temp0
	else:
		temp1 = temp0
	temp2 = -1 * prey[1]
	return [ otherHunter[0] , dist ]
