#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , prey[0] )
	if otherHunter[0] != 0:
		temp1 = temp0 / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp0 = prey[1] + temp0
	temp0 = temp0 - prey[1]
	temp2 = min( dist , prey[1] )
	if dist != 0:
		temp1 = otherHunter[0] / dist
	else:
		temp1 = dist
	temp1 = dist - temp2
	temp2 = otherHunter[0] * prey[1]
	temp0 = -1 * temp1
	temp2 = dist + temp2
	if dist != 0:
		temp3 = otherHunter[1] % dist
	else:
		temp3 = dist
	temp4 = min( prey[0] , prey[0] )
	if temp0 > otherHunter[0] :
		temp3 = min( temp1 , dist )
	else:
		temp3 = temp1 * temp1
	temp5 = max( otherHunter[1] , prey[1] )
	if temp1 > temp5 :
		if otherHunter[1] != 0:
			temp2 = prey[0] % otherHunter[1]
		else:
			temp2 = otherHunter[1]
	else:
		temp2 = dist + temp1
	if temp2 > otherHunter[1] :
		temp2 = otherHunter[1] * dist
	else:
		if prey[1] > temp4 :
			if temp4 != 0:
				temp2 = prey[0] % temp4
			else:
				temp2 = temp4
		else:
			temp2 = max( otherHunter[1] , temp0 )
	if prey[0] > temp3 :
		temp4 = max( prey[0] , temp0 )
	else:
		if temp3 > otherHunter[0] :
			temp4 = temp3 * temp3
		else:
			if otherHunter[0] != 0:
				temp4 = temp2 / otherHunter[0]
			else:
				temp4 = otherHunter[0]
	if temp5 != 0:
		temp3 = otherHunter[1] % temp5
	else:
		temp3 = temp5
	if temp5 != 0:
		temp4 = temp3 % temp5
	else:
		temp4 = temp5
	temp0 = temp5 * temp3
	temp4 = prey[1] * dist
	temp4 = dist * temp2
	temp2 = prey[1] * prey[1]
	temp4 = temp0 * temp0
	if prey[0] != 0:
		temp5 = temp3 % prey[0]
	else:
		temp5 = prey[0]
	return [ temp5 , temp4 ]
