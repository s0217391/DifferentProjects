#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = otherHunter[0] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * dist
	if otherHunter[1] != 0:
		temp0 = otherHunter[0] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp2 = otherHunter[1] - otherHunter[0]
	temp0 = dist * prey[0]
	if otherHunter[0] != 0:
		temp1 = temp1 % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp2 = min( prey[0] , prey[0] )
	if prey[0] != 0:
		temp0 = dist % prey[0]
	else:
		temp0 = prey[0]
	temp2 = min( temp0 , otherHunter[0] )
	temp0 = max( temp1 , temp2 )
	temp2 = min( temp1 , otherHunter[1] )
	if temp2 != 0:
		temp0 = otherHunter[0] % temp2
	else:
		temp0 = temp2
	temp0 = otherHunter[0] - temp0
	temp1 = temp1 * prey[0]
	return [ temp2 , otherHunter[1] ]
