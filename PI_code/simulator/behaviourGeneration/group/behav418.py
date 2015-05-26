#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > otherHunter[1] :
		temp0 = prey[0] + otherHunter[0]
	else:
		temp0 = prey[1] * prey[0]
	temp1 = -1 * prey[0]
	if otherHunter[1] != 0:
		temp1 = temp0 % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp0 = min( temp1 , otherHunter[0] )
	temp2 = prey[0] * prey[1]
	if otherHunter[0] != 0:
		temp3 = otherHunter[0] % otherHunter[0]
	else:
		temp3 = otherHunter[0]
	temp3 = temp1 - temp2
	if prey[0] != 0:
		temp4 = otherHunter[0] % prey[0]
	else:
		temp4 = prey[0]
	temp5 = min( temp1 , temp3 )
	temp0 = prey[1] * dist
	if dist != 0:
		temp1 = otherHunter[0] / dist
	else:
		temp1 = dist
	temp1 = max( temp5 , temp0 )
	temp5 = max( temp4 , prey[0] )
	temp2 = otherHunter[0] * temp1
	temp3 = temp3 + temp0
	temp0 = prey[1] - prey[1]
	if dist > temp5 :
		temp0 = -1 * temp5
	else:
		if dist != 0:
			temp0 = temp1 % dist
		else:
			temp0 = dist
	temp0 = -1 * temp1
	if prey[0] != 0:
		temp0 = dist % prey[0]
	else:
		temp0 = prey[0]
	if prey[1] > prey[0] :
		if temp2 > prey[0] :
			if prey[0] != 0:
				temp4 = prey[1] % prey[0]
			else:
				temp4 = prey[0]
		else:
			temp4 = prey[1] + temp5
	else:
		temp4 = -1 * temp4
	temp6 = temp5 * temp4
	temp2 = -1 * otherHunter[0]
	temp1 = temp0 - temp1
	if prey[0] != 0:
		temp6 = temp5 % prey[0]
	else:
		temp6 = prey[0]
	return [ temp4 , temp4 ]
