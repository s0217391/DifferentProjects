#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = otherHunter[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if prey[1] != 0:
		temp1 = prey[1] / prey[1]
	else:
		temp1 = prey[1]
	temp0 = min( prey[0] , otherHunter[0] )
	temp2 = prey[1] + temp1
	return [ otherHunter[0] , temp2 ]
