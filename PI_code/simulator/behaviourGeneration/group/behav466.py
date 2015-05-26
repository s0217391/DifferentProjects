#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] - prey[0]
	if otherHunter[0] != 0:
		temp1 = temp0 % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp2 = temp1 * otherHunter[1]
	temp0 = -1 * otherHunter[0]
	temp2 = otherHunter[1] + otherHunter[1]
	temp3 = max( prey[0] , otherHunter[0] )
	if prey[0] > otherHunter[1] :
		temp3 = dist - temp3
	else:
		temp3 = -1 * otherHunter[1]
	return [ otherHunter[0] , dist ]
