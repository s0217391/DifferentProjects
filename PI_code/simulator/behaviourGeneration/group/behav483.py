#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * dist
	temp1 = max( prey[1] , prey[1] )
	temp2 = otherHunter[0] + prey[0]
	if dist != 0:
		temp1 = dist / dist
	else:
		temp1 = dist
	temp3 = dist * dist
	temp1 = prey[0] + dist
	temp0 = temp2 * prey[0]
	if temp3 != 0:
		temp3 = dist / temp3
	else:
		temp3 = temp3
	if temp2 > prey[0] :
		temp2 = otherHunter[1] - otherHunter[1]
	else:
		if temp1 != 0:
			temp2 = otherHunter[1] % temp1
		else:
			temp2 = temp1
	temp3 = max( temp2 , otherHunter[0] )
	temp3 = min( prey[0] , temp0 )
	temp3 = prey[0] + temp1
	if otherHunter[1] > temp2 :
		temp2 = temp1 * temp1
	else:
		temp2 = prey[1] * temp3
	temp4 = max( temp0 , otherHunter[0] )
	return [ dist , temp3 ]
