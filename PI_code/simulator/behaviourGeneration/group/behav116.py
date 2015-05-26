#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist - prey[0]
	temp1 = -1 * otherHunter[1]
	temp2 = max( prey[1] , temp1 )
	temp3 = -1 * dist
	if temp2 > temp2 :
		if otherHunter[1] != 0:
			temp0 = dist / otherHunter[1]
		else:
			temp0 = otherHunter[1]
	else:
		if temp3 != 0:
			temp0 = temp0 / temp3
		else:
			temp0 = temp3
	if otherHunter[1] > dist :
		if temp1 != 0:
			temp1 = temp0 % temp1
		else:
			temp1 = temp1
	else:
		if temp1 > otherHunter[0] :
			temp1 = -1 * temp3
		else:
			temp1 = prey[0] * dist
	if prey[1] != 0:
		temp0 = temp3 / prey[1]
	else:
		temp0 = prey[1]
	temp4 = otherHunter[0] * otherHunter[1]
	temp5 = prey[0] - prey[1]
	if temp4 > temp0 :
		temp4 = max( temp0 , temp0 )
	else:
		temp4 = -1 * otherHunter[1]
	temp6 = min( prey[1] , prey[0] )
	if temp1 > temp0 :
		temp1 = temp0 + temp2
	else:
		temp1 = -1 * prey[0]
	if temp1 != 0:
		temp0 = temp2 % temp1
	else:
		temp0 = temp1
	temp5 = temp6 + temp4
	temp5 = temp6 - prey[0]
	temp1 = temp4 - temp5
	temp5 = prey[0] + temp6
	if otherHunter[0] != 0:
		temp0 = temp1 / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if dist != 0:
		temp3 = temp3 / dist
	else:
		temp3 = dist
	temp4 = temp0 * prey[0]
	temp1 = -1 * temp4
	temp3 = otherHunter[1] * temp2
	temp3 = max( temp4 , prey[0] )
	return [ temp0 , temp4 ]
