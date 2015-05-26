#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] > dist :
		temp0 = -1 * otherHunter[0]
	else:
		if dist != 0:
			temp0 = otherHunter[1] / dist
		else:
			temp0 = dist
	if prey[0] != 0:
		temp1 = prey[1] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = otherHunter[0] - otherHunter[0]
	temp2 = prey[1] - temp2
	if dist != 0:
		temp0 = temp0 % dist
	else:
		temp0 = dist
	temp3 = max( temp1 , temp2 )
	temp1 = temp0 + temp2
	if temp1 != 0:
		temp1 = temp2 / temp1
	else:
		temp1 = temp1
	if temp1 != 0:
		temp2 = prey[0] % temp1
	else:
		temp2 = temp1
	if prey[0] != 0:
		temp2 = temp0 / prey[0]
	else:
		temp2 = prey[0]
	if temp3 != 0:
		temp3 = temp0 / temp3
	else:
		temp3 = temp3
	temp1 = min( otherHunter[0] , temp0 )
	if temp1 != 0:
		temp0 = prey[0] % temp1
	else:
		temp0 = temp1
	temp4 = -1 * temp1
	temp2 = temp1 - dist
	temp4 = prey[0] - temp4
	temp0 = min( temp2 , otherHunter[1] )
	temp1 = max( prey[0] , temp3 )
	if otherHunter[1] != 0:
		temp3 = temp4 / otherHunter[1]
	else:
		temp3 = otherHunter[1]
	return [ prey[1] , temp4 ]
