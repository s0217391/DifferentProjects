#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] - otherHunter[1]
	if prey[0] > prey[0] :
		temp1 = prey[0] - otherHunter[0]
	else:
		temp1 = temp0 - temp0
	if temp1 > temp1 :
		if temp0 != 0:
			temp0 = otherHunter[1] / temp0
		else:
			temp0 = temp0
	else:
		temp0 = min( otherHunter[1] , otherHunter[0] )
	temp0 = min( temp0 , prey[0] )
	temp1 = otherHunter[0] + dist
	temp0 = max( otherHunter[0] , otherHunter[0] )
	if otherHunter[1] != 0:
		temp1 = otherHunter[1] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp1 = -1 * temp1
	temp2 = temp0 + prey[1]
	temp2 = dist + otherHunter[0]
	temp0 = -1 * temp0
	temp1 = max( otherHunter[1] , temp2 )
	return [ temp0 , temp2 ]
