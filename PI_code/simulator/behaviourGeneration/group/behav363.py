#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[1] , otherHunter[1] )
	temp1 = -1 * otherHunter[1]
	temp2 = dist * prey[1]
	temp0 = min( prey[0] , dist )
	temp3 = prey[0] - dist
	temp4 = -1 * prey[1]
	temp0 = temp0 + temp3
	if dist != 0:
		temp0 = otherHunter[1] % dist
	else:
		temp0 = dist
	temp3 = otherHunter[0] - prey[1]
	temp2 = -1 * prey[0]
	temp4 = min( temp0 , temp4 )
	temp1 = max( temp3 , prey[0] )
	if prey[0] != 0:
		temp5 = dist / prey[0]
	else:
		temp5 = prey[0]
	if temp5 != 0:
		temp4 = temp2 / temp5
	else:
		temp4 = temp5
	if prey[0] != 0:
		temp3 = prey[0] % prey[0]
	else:
		temp3 = prey[0]
	temp5 = temp4 + dist
	temp1 = min( temp5 , temp1 )
	if temp3 != 0:
		temp5 = temp5 % temp3
	else:
		temp5 = temp3
	temp4 = dist + temp3
	temp4 = max( prey[1] , temp3 )
	return [ temp1 , temp3 ]
