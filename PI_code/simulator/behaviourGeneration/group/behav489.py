#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = prey[1] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = min( otherHunter[0] , otherHunter[1] )
	temp1 = prey[0] * otherHunter[1]
	temp2 = min( prey[0] , temp0 )
	temp1 = temp0 + temp2
	return [ prey[1] , otherHunter[1] ]
