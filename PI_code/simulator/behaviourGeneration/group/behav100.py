#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] - prey[1]
	temp1 = min( otherHunter[1] , otherHunter[0] )
	if temp1 != 0:
		temp1 = otherHunter[0] / temp1
	else:
		temp1 = temp1
	temp2 = temp1 - temp0
	if otherHunter[1] != 0:
		temp2 = prey[0] % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp0 = -1 * otherHunter[1]
	if otherHunter[0] != 0:
		temp3 = temp2 / otherHunter[0]
	else:
		temp3 = otherHunter[0]
	if temp3 > temp0 :
		temp0 = prey[0] + dist
	else:
		temp0 = min( otherHunter[0] , otherHunter[0] )
	temp2 = otherHunter[0] - prey[0]
	if temp1 != 0:
		temp2 = prey[1] % temp1
	else:
		temp2 = temp1
	if temp0 != 0:
		temp4 = prey[0] / temp0
	else:
		temp4 = temp0
	temp0 = temp0 - prey[1]
	return [ temp2 , prey[1] ]
