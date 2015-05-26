#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = dist / dist
	else:
		temp0 = dist
	if dist != 0:
		temp1 = dist % dist
	else:
		temp1 = dist
	temp1 = prey[0] - otherHunter[1]
	temp2 = dist + prey[0]
	temp0 = prey[1] - temp1
	temp2 = max( otherHunter[0] , otherHunter[1] )
	temp0 = otherHunter[0] + prey[1]
	if temp1 > temp1 :
		if temp0 > prey[1] :
			temp2 = -1 * temp2
		else:
			temp2 = otherHunter[0] - temp2
	else:
		temp2 = prey[0] * otherHunter[0]
	temp3 = temp1 + otherHunter[0]
	temp4 = max( otherHunter[0] , prey[0] )
	temp4 = max( temp3 , temp4 )
	temp4 = otherHunter[1] + temp1
	temp2 = temp1 - temp1
	return [ prey[1] , temp2 ]
