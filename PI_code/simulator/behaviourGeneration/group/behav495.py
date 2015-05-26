#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = dist % dist
	else:
		temp0 = dist
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	temp0 = min( otherHunter[1] , otherHunter[0] )
	temp1 = min( prey[1] , temp1 )
	if temp1 != 0:
		temp2 = otherHunter[0] % temp1
	else:
		temp2 = temp1
	if otherHunter[0] > temp0 :
		temp1 = min( otherHunter[1] , otherHunter[1] )
	else:
		if prey[0] != 0:
			temp1 = temp0 / prey[0]
		else:
			temp1 = prey[0]
	temp0 = otherHunter[1] * prey[1]
	temp0 = -1 * dist
	if prey[0] != 0:
		temp1 = temp1 % prey[0]
	else:
		temp1 = prey[0]
	temp1 = max( otherHunter[1] , temp0 )
	temp3 = -1 * temp2
	temp2 = temp0 + temp2
	temp2 = temp2 * dist
	temp3 = otherHunter[1] * dist
	temp2 = max( temp1 , temp0 )
	temp3 = -1 * temp0
	temp3 = temp2 * temp1
	return [ temp0 , prey[1] ]
