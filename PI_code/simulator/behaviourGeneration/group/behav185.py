#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist * otherHunter[1]
	temp1 = -1 * otherHunter[1]
	if prey[0] > otherHunter[0] :
		temp2 = min( dist , temp0 )
	else:
		temp2 = otherHunter[0] + prey[0]
	if prey[0] > prey[0] :
		if temp1 != 0:
			temp3 = dist % temp1
		else:
			temp3 = temp1
	else:
		temp3 = max( temp0 , temp0 )
	if temp0 != 0:
		temp3 = prey[1] % temp0
	else:
		temp3 = temp0
	temp3 = prey[1] * temp0
	if temp1 != 0:
		temp3 = otherHunter[1] % temp1
	else:
		temp3 = temp1
	if otherHunter[0] != 0:
		temp2 = temp2 / otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp1 = otherHunter[0] * temp2
	return [ prey[0] , temp3 ]
