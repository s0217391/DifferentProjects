#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] > prey[1] :
		temp0 = -1 * dist
	else:
		if otherHunter[0] > prey[0] :
			temp0 = min( prey[0] , prey[1] )
		else:
			temp0 = max( prey[0] , otherHunter[1] )
	temp1 = otherHunter[0] + otherHunter[1]
	if temp1 != 0:
		temp1 = temp0 % temp1
	else:
		temp1 = temp1
	temp2 = max( otherHunter[1] , prey[0] )
	if otherHunter[0] > prey[1] :
		if otherHunter[1] > otherHunter[0] :
			temp3 = temp1 - dist
		else:
			if temp0 != 0:
				temp3 = dist % temp0
			else:
				temp3 = temp0
	else:
		temp3 = -1 * temp1
	temp4 = -1 * dist
	temp3 = temp4 - otherHunter[1]
	temp3 = temp2 - dist
	temp2 = temp4 - prey[1]
	temp1 = temp1 * otherHunter[0]
	if temp1 != 0:
		temp3 = dist / temp1
	else:
		temp3 = temp1
	if temp3 != 0:
		temp5 = temp3 % temp3
	else:
		temp5 = temp3
	if temp5 != 0:
		temp2 = temp3 % temp5
	else:
		temp2 = temp5
	temp0 = max( prey[1] , dist )
	return [ prey[0] , otherHunter[0] ]
