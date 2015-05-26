#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > dist :
		temp0 = prey[1] - otherHunter[0]
	else:
		temp0 = dist * dist
	temp1 = max( temp0 , otherHunter[0] )
	temp2 = temp0 * temp0
	temp3 = -1 * dist
	temp0 = otherHunter[0] * temp3
	temp3 = min( temp2 , otherHunter[0] )
	temp3 = temp2 + temp3
	if prey[1] > prey[0] :
		temp0 = -1 * temp0
	else:
		temp0 = temp3 - temp1
	temp4 = min( temp1 , dist )
	if temp4 != 0:
		temp4 = temp1 / temp4
	else:
		temp4 = temp4
	if dist > prey[1] :
		if otherHunter[0] != 0:
			temp1 = prey[0] / otherHunter[0]
		else:
			temp1 = otherHunter[0]
	else:
		temp1 = -1 * temp3
	temp5 = -1 * temp4
	temp4 = min( otherHunter[0] , temp2 )
	temp1 = temp5 - temp4
	temp4 = temp4 * temp4
	temp4 = max( prey[1] , temp5 )
	temp0 = -1 * temp5
	temp2 = temp3 + prey[1]
	temp4 = max( prey[0] , temp4 )
	temp1 = max( prey[0] , temp4 )
	if prey[1] > dist :
		temp3 = min( temp3 , prey[1] )
	else:
		if dist != 0:
			temp3 = temp4 % dist
		else:
			temp3 = dist
	temp3 = -1 * dist
	temp3 = otherHunter[0] - otherHunter[0]
	return [ temp2 , temp5 ]
