#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	temp1 = max( prey[0] , prey[1] )
	temp2 = -1 * temp0
	if temp1 > temp2 :
		if prey[1] != 0:
			temp0 = temp1 % prey[1]
		else:
			temp0 = prey[1]
	else:
		if otherHunter[0] != 0:
			temp0 = otherHunter[1] / otherHunter[0]
		else:
			temp0 = otherHunter[0]
	temp2 = max( prey[0] , temp0 )
	temp3 = dist - otherHunter[0]
	temp1 = temp1 + temp3
	temp1 = temp0 - prey[1]
	temp0 = max( otherHunter[1] , temp2 )
	if prey[0] != 0:
		temp4 = otherHunter[0] / prey[0]
	else:
		temp4 = prey[0]
	if otherHunter[1] > temp4 :
		if prey[0] != 0:
			temp4 = prey[0] / prey[0]
		else:
			temp4 = prey[0]
	else:
		temp4 = min( temp1 , otherHunter[1] )
	temp1 = -1 * temp0
	temp5 = dist * otherHunter[0]
	if temp3 != 0:
		temp6 = dist / temp3
	else:
		temp6 = temp3
	temp5 = -1 * dist
	temp1 = -1 * prey[0]
	if temp1 > otherHunter[0] :
		if prey[1] > temp2 :
			temp2 = temp4 * temp5
		else:
			temp2 = dist - prey[0]
	else:
		temp2 = max( temp3 , otherHunter[1] )
	if otherHunter[1] > temp0 :
		temp0 = min( prey[1] , otherHunter[0] )
	else:
		if temp0 != 0:
			temp0 = temp6 / temp0
		else:
			temp0 = temp0
	temp1 = temp1 - temp0
	temp1 = otherHunter[0] - temp6
	temp1 = otherHunter[0] - temp4
	return [ dist , temp1 ]
