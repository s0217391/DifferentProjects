#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , otherHunter[1] )
	if dist > otherHunter[0] :
		if temp0 != 0:
			temp1 = otherHunter[0] % temp0
		else:
			temp1 = temp0
	else:
		temp1 = temp0 * dist
	temp1 = -1 * temp1
	temp1 = temp1 + prey[1]
	temp0 = max( temp0 , temp1 )
	if temp0 > prey[0] :
		temp1 = temp0 * temp1
	else:
		if otherHunter[1] != 0:
			temp1 = otherHunter[0] / otherHunter[1]
		else:
			temp1 = otherHunter[1]
	temp1 = min( temp1 , temp1 )
	temp1 = min( otherHunter[0] , temp1 )
	temp2 = max( temp1 , otherHunter[1] )
	if temp1 != 0:
		temp2 = dist / temp1
	else:
		temp2 = temp1
	if temp2 != 0:
		temp2 = temp1 / temp2
	else:
		temp2 = temp2
	temp1 = min( otherHunter[1] , otherHunter[0] )
	temp3 = temp0 - otherHunter[0]
	temp1 = -1 * temp1
	return [ temp1 , temp3 ]
