#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = prey[1] / dist
	else:
		temp0 = dist
	if dist > prey[0] :
		if dist != 0:
			temp1 = prey[1] % dist
		else:
			temp1 = dist
	else:
		temp1 = max( dist , otherHunter[1] )
	if temp1 != 0:
		temp0 = temp0 / temp1
	else:
		temp0 = temp1
	temp1 = temp0 + prey[0]
	temp0 = min( otherHunter[1] , prey[0] )
	if otherHunter[0] > prey[0] :
		temp0 = temp1 + otherHunter[0]
	else:
		temp0 = prey[0] + temp1
	temp1 = min( otherHunter[0] , temp0 )
	if prey[0] > prey[0] :
		if prey[0] != 0:
			temp0 = otherHunter[1] % prey[0]
		else:
			temp0 = prey[0]
	else:
		if dist != 0:
			temp0 = temp0 / dist
		else:
			temp0 = dist
	if prey[0] != 0:
		temp2 = dist / prey[0]
	else:
		temp2 = prey[0]
	if prey[1] != 0:
		temp3 = temp2 % prey[1]
	else:
		temp3 = prey[1]
	if otherHunter[1] > temp3 :
		temp2 = -1 * otherHunter[1]
	else:
		if temp1 != 0:
			temp2 = otherHunter[0] % temp1
		else:
			temp2 = temp1
	if temp0 != 0:
		temp0 = otherHunter[1] / temp0
	else:
		temp0 = temp0
	temp1 = temp3 - prey[0]
	if prey[1] != 0:
		temp3 = dist / prey[1]
	else:
		temp3 = prey[1]
	if prey[0] > otherHunter[0] :
		if temp3 > otherHunter[1] :
			temp4 = -1 * dist
		else:
			if temp2 != 0:
				temp4 = prey[1] % temp2
			else:
				temp4 = temp2
	else:
		temp4 = -1 * prey[0]
	temp5 = temp0 * otherHunter[1]
	temp0 = min( otherHunter[1] , otherHunter[1] )
	if temp5 > temp5 :
		if temp4 != 0:
			temp5 = otherHunter[0] / temp4
		else:
			temp5 = temp4
	else:
		if dist != 0:
			temp5 = otherHunter[0] % dist
		else:
			temp5 = dist
	return [ prey[0] , dist ]
