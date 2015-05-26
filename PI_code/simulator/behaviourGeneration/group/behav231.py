#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * dist
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	if prey[0] != 0:
		temp1 = temp0 % prey[0]
	else:
		temp1 = prey[0]
	if temp1 != 0:
		temp0 = otherHunter[1] % temp1
	else:
		temp0 = temp1
	if prey[0] != 0:
		temp1 = otherHunter[0] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = max( prey[1] , temp1 )
	temp2 = min( temp1 , prey[0] )
	if otherHunter[1] != 0:
		temp1 = temp1 % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp3 = temp2 + dist
	temp0 = temp0 * prey[0]
	temp2 = -1 * temp2
	temp1 = dist - temp0
	temp1 = -1 * dist
	temp1 = temp1 - temp2
	temp0 = -1 * dist
	if temp2 != 0:
		temp3 = otherHunter[0] % temp2
	else:
		temp3 = temp2
	if otherHunter[1] != 0:
		temp4 = dist % otherHunter[1]
	else:
		temp4 = otherHunter[1]
	temp5 = dist - dist
	if temp2 != 0:
		temp3 = temp5 % temp2
	else:
		temp3 = temp2
	return [ temp3 , prey[1] ]
