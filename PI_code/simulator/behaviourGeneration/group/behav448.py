#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , prey[1] )
	temp1 = -1 * temp0
	temp2 = prey[1] + temp1
	temp3 = prey[1] + prey[1]
	if temp0 != 0:
		temp3 = temp2 / temp0
	else:
		temp3 = temp0
	temp3 = -1 * otherHunter[0]
	temp3 = min( otherHunter[0] , otherHunter[1] )
	temp0 = max( temp1 , otherHunter[1] )
	if dist != 0:
		temp0 = temp2 / dist
	else:
		temp0 = dist
	temp0 = max( temp1 , temp2 )
	if temp2 != 0:
		temp1 = temp0 / temp2
	else:
		temp1 = temp2
	temp4 = min( temp0 , temp0 )
	return [ temp4 , prey[1] ]
