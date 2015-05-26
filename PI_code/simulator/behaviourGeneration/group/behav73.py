#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	if otherHunter[1] != 0:
		temp1 = dist % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp1 = min( dist , temp0 )
	if otherHunter[0] != 0:
		temp1 = otherHunter[0] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	return [ otherHunter[0] , temp0 ]
