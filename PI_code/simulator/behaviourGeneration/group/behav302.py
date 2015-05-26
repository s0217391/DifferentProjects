#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] > otherHunter[1] :
		temp0 = prey[0] * prey[1]
	else:
		temp0 = max( dist , prey[1] )
	if prey[1] != 0:
		temp1 = dist / prey[1]
	else:
		temp1 = prey[1]
	temp2 = temp0 - otherHunter[1]
	temp0 = -1 * otherHunter[0]
	temp3 = temp1 - dist
	temp1 = otherHunter[0] + prey[0]
	temp4 = min( prey[0] , prey[0] )
	if temp0 != 0:
		temp5 = temp4 % temp0
	else:
		temp5 = temp0
	temp2 = dist - temp4
	temp1 = max( temp1 , otherHunter[1] )
	temp5 = -1 * otherHunter[1]
	if dist != 0:
		temp6 = otherHunter[1] / dist
	else:
		temp6 = dist
	return [ dist , prey[1] ]
