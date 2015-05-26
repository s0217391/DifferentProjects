#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = otherHunter[1] / dist
	else:
		temp0 = dist
	temp1 = max( dist , prey[0] )
	temp1 = -1 * otherHunter[0]
	temp1 = otherHunter[0] - temp0
	temp2 = max( prey[0] , otherHunter[1] )
	temp1 = -1 * dist
	temp3 = min( temp0 , otherHunter[1] )
	if temp2 != 0:
		temp4 = otherHunter[0] / temp2
	else:
		temp4 = temp2
	temp2 = dist - temp1
	if prey[0] != 0:
		temp2 = temp3 % prey[0]
	else:
		temp2 = prey[0]
	if temp1 != 0:
		temp5 = temp2 % temp1
	else:
		temp5 = temp1
	if temp0 != 0:
		temp1 = temp5 % temp0
	else:
		temp1 = temp0
	if prey[1] > dist :
		temp5 = min( dist , prey[0] )
	else:
		temp5 = min( temp0 , temp4 )
	temp4 = temp0 - temp5
	return [ temp0 , prey[1] ]
