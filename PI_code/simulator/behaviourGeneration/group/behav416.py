#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * prey[1]
	temp1 = temp0 + temp0
	temp2 = otherHunter[1] + prey[1]
	temp1 = temp1 - temp0
	temp3 = min( otherHunter[1] , otherHunter[0] )
	temp3 = -1 * dist
	if temp0 > temp2 :
		temp3 = temp3 - temp2
	else:
		temp3 = -1 * prey[1]
	if temp3 != 0:
		temp4 = prey[0] / temp3
	else:
		temp4 = temp3
	if temp1 != 0:
		temp2 = temp3 % temp1
	else:
		temp2 = temp1
	temp3 = temp4 - otherHunter[0]
	if temp4 > temp1 :
		if temp3 > temp1 :
			temp0 = temp1 - prey[1]
		else:
			temp0 = otherHunter[1] + temp3
	else:
		if prey[0] != 0:
			temp0 = dist % prey[0]
		else:
			temp0 = prey[0]
	if dist != 0:
		temp3 = otherHunter[1] / dist
	else:
		temp3 = dist
	temp4 = -1 * temp2
	if otherHunter[1] != 0:
		temp0 = temp0 % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = prey[1] - otherHunter[1]
	temp2 = -1 * temp2
	temp0 = min( temp1 , temp3 )
	temp5 = max( prey[1] , otherHunter[0] )
	if temp5 > dist :
		if temp2 != 0:
			temp3 = temp0 % temp2
		else:
			temp3 = temp2
	else:
		temp3 = otherHunter[0] - temp2
	temp5 = min( otherHunter[0] , temp3 )
	return [ dist , temp1 ]
