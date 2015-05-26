#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + prey[0]
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	temp2 = -1 * temp0
	temp0 = otherHunter[0] - prey[1]
	temp1 = dist * temp1
	temp2 = otherHunter[1] + dist
	temp3 = max( temp2 , otherHunter[1] )
	if temp2 > temp1 :
		temp4 = max( temp3 , temp2 )
	else:
		temp4 = min( temp1 , temp2 )
	temp1 = temp2 + temp0
	if dist != 0:
		temp5 = temp2 % dist
	else:
		temp5 = dist
	temp3 = -1 * temp4
	if temp0 != 0:
		temp6 = temp3 % temp0
	else:
		temp6 = temp0
	return [ otherHunter[0] , temp4 ]
