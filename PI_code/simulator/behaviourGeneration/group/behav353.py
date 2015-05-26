#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist - dist
	temp1 = max( prey[1] , prey[0] )
	temp0 = prey[0] - otherHunter[0]
	temp0 = prey[1] - temp1
	temp2 = -1 * otherHunter[0]
	if otherHunter[0] != 0:
		temp3 = otherHunter[0] / otherHunter[0]
	else:
		temp3 = otherHunter[0]
	temp3 = prey[0] * temp3
	temp1 = temp3 + otherHunter[1]
	temp3 = min( temp2 , otherHunter[0] )
	temp4 = -1 * temp0
	if prey[0] > temp3 :
		if prey[1] != 0:
			temp4 = temp3 % prey[1]
		else:
			temp4 = prey[1]
	else:
		temp4 = min( temp2 , temp3 )
	temp0 = dist - prey[1]
	if temp3 != 0:
		temp2 = temp1 / temp3
	else:
		temp2 = temp3
	if temp0 > dist :
		if dist != 0:
			temp1 = dist % dist
		else:
			temp1 = dist
	else:
		temp1 = otherHunter[0] - temp0
	temp1 = min( prey[1] , temp4 )
	temp3 = prey[1] - otherHunter[1]
	temp3 = min( prey[1] , temp2 )
	if dist != 0:
		temp1 = otherHunter[1] % dist
	else:
		temp1 = dist
	temp3 = temp3 * temp3
	if temp2 != 0:
		temp4 = otherHunter[0] / temp2
	else:
		temp4 = temp2
	if temp1 != 0:
		temp1 = otherHunter[1] % temp1
	else:
		temp1 = temp1
	temp4 = -1 * temp1
	temp1 = max( temp2 , dist )
	return [ prey[1] , temp1 ]
