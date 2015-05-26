#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , otherHunter[1] )
	temp1 = -1 * prey[1]
	temp2 = min( temp1 , otherHunter[1] )
	temp0 = temp0 - dist
	temp3 = min( dist , otherHunter[0] )
	temp0 = min( otherHunter[0] , prey[1] )
	temp4 = -1 * otherHunter[1]
	if temp2 > prey[0] :
		temp5 = min( temp3 , prey[0] )
	else:
		if otherHunter[0] != 0:
			temp5 = temp2 / otherHunter[0]
		else:
			temp5 = otherHunter[0]
	temp2 = prey[0] * temp5
	if otherHunter[1] != 0:
		temp4 = temp5 / otherHunter[1]
	else:
		temp4 = otherHunter[1]
	temp0 = otherHunter[0] * otherHunter[1]
	if temp4 > temp3 :
		temp6 = temp4 * otherHunter[0]
	else:
		if temp0 != 0:
			temp6 = temp5 % temp0
		else:
			temp6 = temp0
	temp4 = min( otherHunter[1] , temp3 )
	temp7 = prey[1] - otherHunter[1]
	if temp5 > temp2 :
		temp3 = prey[0] - temp7
	else:
		temp3 = min( temp7 , prey[1] )
	temp2 = min( dist , otherHunter[1] )
	temp1 = -1 * temp3
	temp7 = temp4 * temp4
	if temp2 != 0:
		temp1 = temp6 / temp2
	else:
		temp1 = temp2
	temp2 = min( prey[1] , prey[1] )
	if temp6 != 0:
		temp1 = prey[1] / temp6
	else:
		temp1 = temp6
	temp3 = max( otherHunter[1] , prey[0] )
	temp2 = max( otherHunter[0] , temp2 )
	return [ dist , temp2 ]
