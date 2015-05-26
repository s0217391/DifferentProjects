#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * dist
	temp1 = temp0 + otherHunter[0]
	temp0 = -1 * otherHunter[1]
	if temp0 > otherHunter[0] :
		temp2 = otherHunter[1] + prey[1]
	else:
		temp2 = min( otherHunter[1] , temp1 )
	if dist != 0:
		temp3 = temp1 / dist
	else:
		temp3 = dist
	temp0 = -1 * temp1
	temp3 = temp1 + otherHunter[1]
	if temp3 != 0:
		temp2 = temp2 / temp3
	else:
		temp2 = temp3
	temp3 = temp2 + temp1
	if otherHunter[0] != 0:
		temp1 = dist / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if temp0 != 0:
		temp2 = prey[0] % temp0
	else:
		temp2 = temp0
	temp2 = temp2 + temp0
	temp1 = min( temp1 , prey[0] )
	if otherHunter[1] > temp0 :
		temp1 = min( temp1 , prey[0] )
	else:
		temp1 = prey[1] * prey[0]
	temp4 = dist * temp0
	temp5 = -1 * temp1
	temp6 = otherHunter[0] * prey[0]
	temp2 = -1 * prey[0]
	temp5 = max( temp1 , temp4 )
	temp7 = -1 * temp4
	return [ prey[1] , temp1 ]
