#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	temp1 = prey[0] * prey[0]
	temp2 = prey[0] * otherHunter[1]
	temp3 = max( otherHunter[1] , prey[1] )
	temp0 = min( dist , temp0 )
	temp1 = prey[0] + prey[0]
	temp1 = -1 * temp1
	temp0 = otherHunter[1] * prey[1]
	temp0 = -1 * dist
	if prey[0] > temp3 :
		if temp1 != 0:
			temp2 = temp3 % temp1
		else:
			temp2 = temp1
	else:
		temp2 = temp0 + dist
	temp0 = min( prey[0] , temp0 )
	temp4 = otherHunter[1] + temp2
	temp5 = prey[1] * temp1
	if otherHunter[1] > temp3 :
		temp0 = max( otherHunter[0] , temp0 )
	else:
		temp0 = -1 * otherHunter[0]
	temp4 = max( temp0 , prey[1] )
	if prey[0] > otherHunter[0] :
		if prey[1] != 0:
			temp1 = prey[0] / prey[1]
		else:
			temp1 = prey[1]
	else:
		temp1 = max( prey[0] , dist )
	temp4 = min( temp5 , temp0 )
	temp4 = min( temp3 , dist )
	if dist != 0:
		temp0 = dist % dist
	else:
		temp0 = dist
	temp5 = max( temp1 , temp1 )
	temp4 = otherHunter[1] - otherHunter[0]
	return [ temp5 , temp2 ]
