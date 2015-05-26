#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = otherHunter[0] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = otherHunter[0] - prey[1]
	temp2 = min( dist , temp1 )
	temp1 = prey[1] - temp1
	if temp1 != 0:
		temp2 = otherHunter[0] % temp1
	else:
		temp2 = temp1
	if temp2 > temp2 :
		temp3 = prey[0] + dist
	else:
		if otherHunter[1] != 0:
			temp3 = dist % otherHunter[1]
		else:
			temp3 = otherHunter[1]
	temp2 = temp3 + otherHunter[0]
	temp3 = -1 * otherHunter[0]
	temp3 = max( prey[0] , temp1 )
	temp1 = temp3 - dist
	temp1 = min( temp0 , temp2 )
	temp3 = prey[1] * temp1
	temp2 = temp1 + dist
	temp0 = prey[1] * prey[0]
	temp3 = min( temp0 , temp1 )
	temp0 = temp1 - temp2
	temp0 = dist - otherHunter[0]
	if temp1 != 0:
		temp4 = dist % temp1
	else:
		temp4 = temp1
	if dist != 0:
		temp5 = otherHunter[1] / dist
	else:
		temp5 = dist
	if otherHunter[1] > temp5 :
		temp4 = temp4 + otherHunter[0]
	else:
		temp4 = otherHunter[0] * prey[0]
	temp5 = temp4 + otherHunter[1]
	temp0 = temp5 * temp2
	temp0 = temp1 * temp3
	temp6 = min( temp3 , otherHunter[0] )
	if temp1 != 0:
		temp4 = temp2 % temp1
	else:
		temp4 = temp1
	return [ otherHunter[1] , prey[0] ]
