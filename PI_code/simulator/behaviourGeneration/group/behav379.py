#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = otherHunter[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[0] + prey[1]
	temp2 = max( temp1 , temp1 )
	return [ otherHunter[0] , temp1 ]
