#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[1]
	temp1 = -1 * dist
	if prey[1] > temp0 :
		temp2 = otherHunter[1] * prey[1]
	else:
		temp2 = otherHunter[0] * otherHunter[1]
	temp2 = -1 * otherHunter[0]
	if otherHunter[1] != 0:
		temp0 = temp1 % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp3 = max( prey[1] , temp2 )
	temp1 = prey[0] - temp1
	temp2 = min( otherHunter[0] , prey[1] )
	temp4 = dist - temp0
	temp3 = -1 * otherHunter[0]
	if otherHunter[1] != 0:
		temp1 = prey[1] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp3 = prey[1] * otherHunter[0]
	if otherHunter[0] != 0:
		temp5 = temp0 / otherHunter[0]
	else:
		temp5 = otherHunter[0]
	temp0 = prey[1] - otherHunter[1]
	temp6 = dist * temp2
	if temp2 != 0:
		temp2 = temp6 % temp2
	else:
		temp2 = temp2
	if temp4 != 0:
		temp5 = dist / temp4
	else:
		temp5 = temp4
	return [ temp1 , temp5 ]
