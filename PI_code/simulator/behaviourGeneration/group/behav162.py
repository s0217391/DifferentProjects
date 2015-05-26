#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , otherHunter[0] )
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	temp2 = max( prey[0] , temp0 )
	if dist > temp2 :
		temp3 = -1 * prey[1]
	else:
		temp3 = min( dist , otherHunter[1] )
	temp4 = prey[0] - temp1
	temp1 = -1 * otherHunter[0]
	if temp2 > temp0 :
		temp3 = max( otherHunter[1] , prey[1] )
	else:
		temp3 = max( temp1 , temp0 )
	temp0 = temp0 - otherHunter[1]
	temp4 = max( otherHunter[0] , temp0 )
	temp4 = -1 * temp1
	temp5 = otherHunter[1] - otherHunter[0]
	if temp1 != 0:
		temp4 = prey[0] / temp1
	else:
		temp4 = temp1
	temp3 = -1 * temp2
	temp2 = otherHunter[1] + temp4
	return [ temp2 , temp4 ]
