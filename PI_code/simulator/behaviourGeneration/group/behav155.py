#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * dist
	temp1 = min( otherHunter[0] , otherHunter[0] )
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp0 = min( dist , dist )
	temp0 = prey[0] * otherHunter[0]
	temp1 = max( otherHunter[1] , temp0 )
	temp0 = prey[1] * otherHunter[0]
	return [ temp1 , temp0 ]
