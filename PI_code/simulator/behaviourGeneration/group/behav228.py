#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > otherHunter[1] :
		temp0 = min( prey[1] , prey[0] )
	else:
		temp0 = dist * otherHunter[1]
	temp1 = min( prey[1] , otherHunter[1] )
	temp0 = prey[0] + prey[0]
	temp0 = -1 * prey[1]
	temp2 = otherHunter[1] + prey[0]
	if dist > dist :
		temp0 = max( otherHunter[0] , prey[1] )
	else:
		temp0 = -1 * temp2
	if dist > otherHunter[0] :
		if temp0 != 0:
			temp2 = temp1 % temp0
		else:
			temp2 = temp0
	else:
		temp2 = dist * temp1
	temp0 = -1 * otherHunter[0]
	if temp1 != 0:
		temp0 = otherHunter[1] % temp1
	else:
		temp0 = temp1
	temp3 = max( otherHunter[0] , prey[1] )
	if otherHunter[0] != 0:
		temp0 = dist % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp0 = max( prey[1] , prey[1] )
	return [ prey[1] , temp0 ]
