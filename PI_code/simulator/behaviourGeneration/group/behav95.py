#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] - otherHunter[0]
	temp1 = -1 * temp0
	temp2 = otherHunter[1] + otherHunter[1]
	if otherHunter[1] != 0:
		temp3 = prey[1] % otherHunter[1]
	else:
		temp3 = otherHunter[1]
	if temp1 != 0:
		temp0 = prey[0] % temp1
	else:
		temp0 = temp1
	if dist > otherHunter[0] :
		if dist > prey[1] :
			temp1 = -1 * temp2
		else:
			temp1 = max( temp2 , temp3 )
	else:
		if prey[0] != 0:
			temp1 = temp1 / prey[0]
		else:
			temp1 = prey[0]
	if temp0 != 0:
		temp4 = prey[1] / temp0
	else:
		temp4 = temp0
	temp4 = prey[1] + temp1
	if temp4 != 0:
		temp1 = temp1 % temp4
	else:
		temp1 = temp4
	temp1 = -1 * dist
	temp3 = -1 * temp1
	if dist != 0:
		temp1 = temp2 / dist
	else:
		temp1 = dist
	temp5 = temp1 * otherHunter[1]
	if temp2 > prey[1] :
		temp3 = max( prey[0] , dist )
	else:
		temp3 = otherHunter[0] + temp4
	if temp3 > temp3 :
		if otherHunter[1] != 0:
			temp0 = dist / otherHunter[1]
		else:
			temp0 = otherHunter[1]
	else:
		if prey[0] != 0:
			temp0 = temp1 / prey[0]
		else:
			temp0 = prey[0]
	return [ temp3 , dist ]
