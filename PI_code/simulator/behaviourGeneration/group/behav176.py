#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist + dist
	if otherHunter[1] != 0:
		temp1 = dist / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if temp0 != 0:
		temp0 = otherHunter[0] % temp0
	else:
		temp0 = temp0
	if temp0 != 0:
		temp1 = otherHunter[1] / temp0
	else:
		temp1 = temp0
	temp1 = max( prey[0] , prey[0] )
	temp1 = otherHunter[0] + temp0
	temp2 = temp0 * temp0
	temp1 = dist * temp2
	if prey[0] > dist :
		temp2 = min( otherHunter[0] , temp0 )
	else:
		temp2 = max( otherHunter[1] , prey[0] )
	temp0 = otherHunter[1] * dist
	if temp0 != 0:
		temp1 = dist % temp0
	else:
		temp1 = temp0
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	if otherHunter[0] != 0:
		temp3 = otherHunter[1] % otherHunter[0]
	else:
		temp3 = otherHunter[0]
	return [ temp2 , temp0 ]
