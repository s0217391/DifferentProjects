#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * otherHunter[0]
	temp1 = temp0 + prey[0]
	temp1 = prey[1] * temp1
	temp2 = -1 * temp1
	temp2 = otherHunter[1] * otherHunter[1]
	temp0 = -1 * otherHunter[0]
	temp1 = -1 * dist
	if otherHunter[1] != 0:
		temp3 = otherHunter[0] / otherHunter[1]
	else:
		temp3 = otherHunter[1]
	temp1 = min( temp3 , temp1 )
	temp2 = dist - temp3
	temp3 = -1 * otherHunter[1]
	temp2 = min( otherHunter[0] , temp2 )
	if otherHunter[0] > prey[0] :
		temp2 = min( otherHunter[1] , temp2 )
	else:
		temp2 = max( temp0 , otherHunter[0] )
	return [ temp0 , dist ]
