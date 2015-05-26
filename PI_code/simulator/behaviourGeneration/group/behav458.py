#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[0]
	if prey[0] != 0:
		temp1 = dist / prey[0]
	else:
		temp1 = prey[0]
	temp1 = prey[1] - otherHunter[0]
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	if temp1 != 0:
		temp0 = dist / temp1
	else:
		temp0 = temp1
	if dist != 0:
		temp0 = prey[1] % dist
	else:
		temp0 = dist
	temp0 = prey[0] * dist
	temp1 = prey[0] * temp0
	temp2 = otherHunter[0] * temp0
	if temp2 != 0:
		temp1 = otherHunter[0] / temp2
	else:
		temp1 = temp2
	temp3 = otherHunter[1] - prey[0]
	temp0 = temp0 - temp3
	temp1 = min( otherHunter[0] , prey[1] )
	if prey[0] != 0:
		temp1 = prey[1] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = temp2 * temp0
	temp4 = temp3 + temp0
	temp2 = prey[0] * temp3
	temp4 = dist * temp4
	temp1 = min( temp4 , temp4 )
	temp1 = max( temp3 , otherHunter[1] )
	return [ temp0 , temp4 ]
