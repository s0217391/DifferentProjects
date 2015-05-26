#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[0] , otherHunter[1] )
	temp1 = dist * temp0
	if prey[1] > temp0 :
		temp0 = max( dist , temp0 )
	else:
		if prey[0] != 0:
			temp0 = temp1 % prey[0]
		else:
			temp0 = prey[0]
	if temp1 != 0:
		temp0 = prey[1] / temp1
	else:
		temp0 = temp1
	temp2 = max( otherHunter[1] , otherHunter[0] )
	if temp0 > dist :
		temp2 = max( dist , otherHunter[0] )
	else:
		temp2 = otherHunter[0] - otherHunter[0]
	temp0 = -1 * prey[1]
	if temp0 != 0:
		temp2 = otherHunter[1] / temp0
	else:
		temp2 = temp0
	if otherHunter[1] != 0:
		temp0 = temp2 / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = min( temp0 , otherHunter[0] )
	temp3 = otherHunter[1] - otherHunter[0]
	if temp0 != 0:
		temp4 = prey[0] % temp0
	else:
		temp4 = temp0
	temp1 = min( prey[0] , temp4 )
	if dist != 0:
		temp2 = otherHunter[0] % dist
	else:
		temp2 = dist
	temp2 = temp4 - otherHunter[0]
	temp0 = min( prey[0] , prey[1] )
	if temp2 > otherHunter[0] :
		if temp2 != 0:
			temp0 = temp1 % temp2
		else:
			temp0 = temp2
	else:
		temp0 = -1 * temp0
	temp4 = dist - prey[1]
	temp5 = min( temp1 , temp0 )
	if otherHunter[0] > otherHunter[0] :
		temp6 = max( dist , dist )
	else:
		temp6 = temp5 * temp3
	temp3 = temp4 + prey[1]
	if prey[1] != 0:
		temp2 = temp4 / prey[1]
	else:
		temp2 = prey[1]
	if dist != 0:
		temp3 = temp6 / dist
	else:
		temp3 = dist
	temp2 = dist + temp4
	if otherHunter[1] > temp5 :
		if temp5 > prey[1] :
			if dist > otherHunter[1] :
				if temp3 != 0:
					temp4 = otherHunter[0] / temp3
				else:
					temp4 = temp3
			else:
				temp4 = max( temp5 , otherHunter[0] )
		else:
			temp4 = max( prey[0] , otherHunter[0] )
	else:
		if temp0 > otherHunter[0] :
			temp4 = min( otherHunter[0] , otherHunter[1] )
		else:
			temp4 = temp5 * otherHunter[0]
	return [ dist , prey[0] ]
