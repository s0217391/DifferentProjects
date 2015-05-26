#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * dist
	temp1 = temp0 * otherHunter[0]
	if otherHunter[1] > otherHunter[0] :
		temp2 = temp0 - temp0
	else:
		if temp1 != 0:
			temp2 = prey[0] / temp1
		else:
			temp2 = temp1
	temp3 = -1 * otherHunter[1]
	temp4 = max( temp1 , otherHunter[1] )
	temp3 = -1 * dist
	temp5 = max( temp0 , prey[0] )
	temp4 = min( temp1 , temp5 )
	temp4 = max( prey[0] , otherHunter[1] )
	temp0 = temp2 * temp2
	if dist > temp5 :
		temp3 = prey[1] - dist
	else:
		temp3 = -1 * prey[0]
	temp4 = temp4 - dist
	temp3 = max( otherHunter[1] , prey[0] )
	temp2 = min( temp0 , temp1 )
	temp6 = temp5 * temp4
	if temp3 != 0:
		temp6 = temp4 / temp3
	else:
		temp6 = temp3
	temp4 = min( dist , temp0 )
	if otherHunter[0] > prey[1] :
		temp7 = -1 * temp5
	else:
		if temp2 != 0:
			temp7 = temp5 / temp2
		else:
			temp7 = temp2
	temp3 = -1 * temp6
	temp0 = min( otherHunter[1] , temp3 )
	return [ otherHunter[1] , temp4 ]
