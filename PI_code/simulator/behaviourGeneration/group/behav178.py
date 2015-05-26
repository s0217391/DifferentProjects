#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , prey[0] )
	if otherHunter[1] > dist :
		if prey[0] != 0:
			temp1 = dist % prey[0]
		else:
			temp1 = prey[0]
	else:
		if otherHunter[0] != 0:
			temp1 = temp0 % otherHunter[0]
		else:
			temp1 = otherHunter[0]
	if temp0 > temp0 :
		if temp0 != 0:
			temp1 = otherHunter[1] / temp0
		else:
			temp1 = temp0
	else:
		temp1 = temp0 + temp1
	temp1 = min( dist , otherHunter[1] )
	if otherHunter[0] != 0:
		temp1 = prey[0] / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if otherHunter[1] != 0:
		temp0 = dist / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp2 = dist * otherHunter[0]
	temp1 = temp0 + temp1
	if otherHunter[0] != 0:
		temp3 = temp0 % otherHunter[0]
	else:
		temp3 = otherHunter[0]
	temp4 = temp1 * temp2
	temp4 = -1 * temp2
	temp2 = temp1 + otherHunter[1]
	temp3 = prey[0] - otherHunter[0]
	if temp3 != 0:
		temp1 = temp4 % temp3
	else:
		temp1 = temp3
	temp4 = temp3 * temp2
	temp0 = prey[1] * prey[0]
	temp4 = otherHunter[1] - prey[0]
	temp0 = temp0 + temp2
	temp5 = temp3 - dist
	temp0 = temp0 + dist
	temp3 = min( otherHunter[1] , temp2 )
	if temp2 != 0:
		temp6 = temp3 / temp2
	else:
		temp6 = temp2
	temp4 = prey[0] * otherHunter[0]
	if temp4 != 0:
		temp3 = prey[1] % temp4
	else:
		temp3 = temp4
	if otherHunter[1] != 0:
		temp3 = temp2 / otherHunter[1]
	else:
		temp3 = otherHunter[1]
	return [ temp4 , temp5 ]
