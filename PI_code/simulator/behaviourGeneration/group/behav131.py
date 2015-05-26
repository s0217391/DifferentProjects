#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] * otherHunter[1]
	temp1 = otherHunter[1] * temp0
	temp2 = otherHunter[0] + dist
	temp1 = -1 * prey[0]
	if temp0 > otherHunter[1] :
		if dist != 0:
			temp3 = temp1 / dist
		else:
			temp3 = dist
	else:
		temp3 = -1 * prey[1]
	temp4 = otherHunter[1] - prey[1]
	temp0 = min( dist , temp2 )
	temp3 = temp4 - otherHunter[0]
	temp1 = min( temp1 , otherHunter[0] )
	temp0 = min( dist , otherHunter[0] )
	temp3 = temp0 - otherHunter[1]
	if dist != 0:
		temp0 = temp1 / dist
	else:
		temp0 = dist
	temp1 = prey[1] + prey[1]
	temp1 = otherHunter[1] - temp3
	return [ prey[1] , otherHunter[0] ]
