#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , otherHunter[0] )
	temp1 = min( temp0 , temp0 )
	temp2 = prey[1] + temp1
	temp2 = -1 * otherHunter[0]
	temp0 = -1 * otherHunter[0]
	temp0 = otherHunter[0] + prey[0]
	if temp0 != 0:
		temp1 = otherHunter[1] / temp0
	else:
		temp1 = temp0
	if otherHunter[0] != 0:
		temp1 = temp1 % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if prey[0] != 0:
		temp1 = temp0 % prey[0]
	else:
		temp1 = prey[0]
	return [ prey[0] , otherHunter[1] ]
