#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[1]
	if dist != 0:
		temp1 = temp0 / dist
	else:
		temp1 = dist
	temp0 = -1 * otherHunter[1]
	temp1 = otherHunter[1] * prey[1]
	if dist != 0:
		temp2 = temp1 % dist
	else:
		temp2 = dist
	temp3 = temp0 + otherHunter[0]
	if temp2 > dist :
		if temp2 != 0:
			temp3 = temp3 % temp2
		else:
			temp3 = temp2
	else:
		if temp1 > otherHunter[1] :
			if temp3 != 0:
				temp3 = prey[0] % temp3
			else:
				temp3 = temp3
		else:
			temp3 = temp3 * prey[1]
	if temp3 != 0:
		temp1 = dist / temp3
	else:
		temp1 = temp3
	if prey[1] > temp2 :
		temp1 = temp1 * temp2
	else:
		temp1 = otherHunter[0] + prey[1]
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp0 = prey[0] + otherHunter[1]
	temp2 = prey[0] + temp3
	temp4 = -1 * otherHunter[0]
	if temp3 != 0:
		temp0 = temp0 % temp3
	else:
		temp0 = temp3
	temp4 = prey[1] + temp1
	temp3 = prey[1] + temp2
	temp1 = max( otherHunter[0] , temp3 )
	temp2 = temp1 + otherHunter[0]
	if dist > otherHunter[0] :
		if prey[0] > prey[0] :
			temp0 = -1 * temp0
		else:
			temp0 = dist + prey[0]
	else:
		if prey[1] != 0:
			temp0 = otherHunter[1] / prey[1]
		else:
			temp0 = prey[1]
	if temp2 != 0:
		temp5 = prey[1] / temp2
	else:
		temp5 = temp2
	return [ prey[1] , temp5 ]
