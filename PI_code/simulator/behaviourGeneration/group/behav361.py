#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] * prey[0]
	temp1 = -1 * dist
	temp0 = temp0 - otherHunter[1]
	temp1 = max( prey[1] , prey[1] )
	if temp1 != 0:
		temp2 = otherHunter[1] % temp1
	else:
		temp2 = temp1
	if dist != 0:
		temp1 = otherHunter[0] / dist
	else:
		temp1 = dist
	if otherHunter[1] != 0:
		temp0 = prey[1] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if temp0 > prey[1] :
		temp1 = temp0 + temp1
	else:
		if temp1 > otherHunter[1] :
			if prey[1] != 0:
				temp1 = otherHunter[1] % prey[1]
			else:
				temp1 = prey[1]
		else:
			temp1 = dist + temp1
	temp2 = prey[0] - temp2
	temp1 = otherHunter[1] - dist
	temp3 = temp2 * otherHunter[1]
	temp2 = temp1 * temp0
	if otherHunter[1] != 0:
		temp0 = otherHunter[1] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if otherHunter[0] > dist :
		if prey[0] != 0:
			temp1 = temp3 / prey[0]
		else:
			temp1 = prey[0]
	else:
		temp1 = max( prey[1] , temp0 )
	temp0 = temp1 + temp1
	if otherHunter[1] != 0:
		temp0 = temp1 % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp0 = temp1 * prey[0]
	temp0 = temp2 * temp2
	if prey[0] != 0:
		temp2 = dist % prey[0]
	else:
		temp2 = prey[0]
	if dist > temp0 :
		if temp0 > prey[0] :
			temp4 = max( temp3 , temp2 )
		else:
			temp4 = min( dist , dist )
	else:
		if temp2 != 0:
			temp4 = otherHunter[1] % temp2
		else:
			temp4 = temp2
	temp2 = temp3 * otherHunter[1]
	temp1 = prey[0] + temp1
	temp3 = min( temp4 , prey[1] )
	if dist != 0:
		temp5 = temp1 % dist
	else:
		temp5 = dist
	return [ temp5 , otherHunter[0] ]
