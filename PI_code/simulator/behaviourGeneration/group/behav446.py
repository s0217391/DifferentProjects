#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] * dist
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	temp1 = prey[0] * otherHunter[1]
	temp2 = dist * dist
	temp3 = temp2 * otherHunter[0]
	temp0 = temp2 * prey[0]
	temp3 = max( otherHunter[1] , otherHunter[0] )
	temp2 = temp3 + otherHunter[1]
	temp2 = temp1 + temp0
	temp1 = min( prey[0] , otherHunter[0] )
	if temp1 > temp2 :
		temp0 = otherHunter[1] * prey[1]
	else:
		if otherHunter[1] > temp2 :
			temp0 = temp0 * otherHunter[0]
		else:
			temp0 = dist * otherHunter[0]
	if prey[0] > otherHunter[1] :
		temp4 = otherHunter[0] - otherHunter[1]
	else:
		temp4 = dist - temp2
	temp3 = max( temp3 , temp2 )
	temp3 = min( temp2 , temp4 )
	temp2 = min( prey[0] , temp3 )
	return [ temp2 , temp3 ]
