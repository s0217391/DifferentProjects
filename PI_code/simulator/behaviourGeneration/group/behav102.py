#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] - dist
	temp1 = prey[1] - prey[1]
	temp2 = otherHunter[0] + prey[0]
	temp1 = otherHunter[1] * otherHunter[1]
	temp1 = temp2 + temp0
	temp1 = min( otherHunter[1] , prey[0] )
	temp1 = max( prey[0] , prey[0] )
	temp2 = prey[1] - prey[1]
	if temp0 != 0:
		temp2 = otherHunter[1] % temp0
	else:
		temp2 = temp0
	temp3 = prey[0] * temp0
	temp0 = temp2 + temp3
	if temp2 != 0:
		temp0 = prey[1] % temp2
	else:
		temp0 = temp2
	if temp3 > temp3 :
		temp0 = prey[0] - temp2
	else:
		temp0 = max( otherHunter[1] , otherHunter[0] )
	temp4 = prey[1] + otherHunter[0]
	temp5 = -1 * prey[0]
	if temp1 > temp0 :
		if otherHunter[0] != 0:
			temp4 = temp2 / otherHunter[0]
		else:
			temp4 = otherHunter[0]
	else:
		temp4 = max( otherHunter[1] , otherHunter[1] )
	return [ temp4 , prey[0] ]
