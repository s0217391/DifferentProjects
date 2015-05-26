#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = prey[1] / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if otherHunter[1] > prey[0] :
		temp1 = -1 * dist
	else:
		if otherHunter[1] != 0:
			temp1 = prey[1] / otherHunter[1]
		else:
			temp1 = otherHunter[1]
	temp1 = otherHunter[1] + temp1
	temp2 = max( otherHunter[0] , otherHunter[1] )
	temp0 = max( temp0 , prey[0] )
	temp1 = otherHunter[0] - prey[1]
	if otherHunter[1] != 0:
		temp3 = dist / otherHunter[1]
	else:
		temp3 = otherHunter[1]
	temp1 = prey[1] + otherHunter[0]
	if temp3 > dist :
		if otherHunter[1] > temp3 :
			temp3 = max( prey[1] , prey[1] )
		else:
			if prey[1] != 0:
				temp3 = dist / prey[1]
			else:
				temp3 = prey[1]
	else:
		temp3 = -1 * temp2
	if dist != 0:
		temp1 = otherHunter[1] % dist
	else:
		temp1 = dist
	if otherHunter[0] > temp3 :
		if prey[1] != 0:
			temp1 = dist / prey[1]
		else:
			temp1 = prey[1]
	else:
		temp1 = temp0 * temp1
	if prey[0] > temp1 :
		temp1 = max( otherHunter[0] , otherHunter[0] )
	else:
		temp1 = -1 * temp2
	if prey[0] > prey[0] :
		if dist > temp0 :
			temp3 = temp1 * temp1
		else:
			if temp3 != 0:
				temp3 = otherHunter[0] % temp3
			else:
				temp3 = temp3
	else:
		temp3 = max( temp3 , temp3 )
	temp2 = -1 * prey[0]
	temp4 = max( temp0 , temp1 )
	temp0 = otherHunter[0] * temp0
	if temp3 > temp2 :
		temp3 = temp3 * temp4
	else:
		temp3 = -1 * prey[1]
	temp2 = -1 * temp4
	return [ dist , temp4 ]
