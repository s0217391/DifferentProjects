#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] > otherHunter[0] :
		if otherHunter[1] != 0:
			temp0 = otherHunter[0] / otherHunter[1]
		else:
			temp0 = otherHunter[1]
	else:
		temp0 = min( otherHunter[1] , dist )
	temp1 = prey[1] + dist
	if temp0 > dist :
		if dist > otherHunter[1] :
			temp1 = temp0 * otherHunter[0]
		else:
			temp1 = otherHunter[0] + prey[1]
	else:
		temp1 = dist - dist
	if dist != 0:
		temp2 = dist % dist
	else:
		temp2 = dist
	if temp0 > otherHunter[1] :
		temp0 = max( prey[0] , prey[1] )
	else:
		temp0 = min( dist , dist )
	temp2 = -1 * temp0
	if dist != 0:
		temp3 = prey[0] / dist
	else:
		temp3 = dist
	temp4 = -1 * temp2
	if temp4 != 0:
		temp5 = temp3 / temp4
	else:
		temp5 = temp4
	temp0 = temp2 * temp2
	if prey[0] != 0:
		temp2 = temp2 % prey[0]
	else:
		temp2 = prey[0]
	temp1 = temp1 * temp3
	temp6 = max( temp1 , temp5 )
	temp3 = max( prey[0] , prey[1] )
	if temp6 != 0:
		temp2 = temp0 % temp6
	else:
		temp2 = temp6
	temp4 = otherHunter[0] * temp1
	if temp6 != 0:
		temp2 = temp1 / temp6
	else:
		temp2 = temp6
	temp0 = -1 * temp0
	temp2 = min( temp6 , temp4 )
	temp4 = temp0 - temp5
	return [ temp6 , otherHunter[0] ]
