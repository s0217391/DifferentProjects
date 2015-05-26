#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[0] , prey[0] )
	if dist != 0:
		temp1 = dist / dist
	else:
		temp1 = dist
	temp1 = min( otherHunter[1] , otherHunter[0] )
	temp2 = max( temp1 , temp0 )
	temp3 = min( dist , prey[1] )
	temp1 = temp1 + temp1
	if temp3 > prey[1] :
		if otherHunter[0] > temp2 :
			temp0 = min( temp0 , prey[0] )
		else:
			temp0 = otherHunter[1] * prey[1]
	else:
		temp0 = -1 * prey[0]
	temp2 = min( temp3 , dist )
	temp0 = temp2 * temp2
	if otherHunter[0] != 0:
		temp4 = dist / otherHunter[0]
	else:
		temp4 = otherHunter[0]
	temp4 = max( otherHunter[0] , otherHunter[0] )
	if otherHunter[1] != 0:
		temp4 = temp3 / otherHunter[1]
	else:
		temp4 = otherHunter[1]
	if temp3 != 0:
		temp1 = prey[1] / temp3
	else:
		temp1 = temp3
	temp0 = temp0 - dist
	temp1 = max( dist , temp2 )
	temp4 = temp3 + temp0
	return [ prey[0] , prey[1] ]
