#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] > prey[0] :
		if prey[0] > prey[1] :
			temp0 = prey[1] + prey[0]
		else:
			temp0 = otherHunter[1] + otherHunter[1]
	else:
		if otherHunter[1] != 0:
			temp0 = otherHunter[0] / otherHunter[1]
		else:
			temp0 = otherHunter[1]
	if temp0 != 0:
		temp1 = dist % temp0
	else:
		temp1 = temp0
	temp1 = max( temp0 , otherHunter[1] )
	temp2 = temp0 * prey[0]
	if dist > prey[1] :
		temp0 = dist + temp2
	else:
		if prey[0] != 0:
			temp0 = prey[0] / prey[0]
		else:
			temp0 = prey[0]
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp0 = otherHunter[1] + temp1
	temp0 = prey[0] + temp0
	temp3 = -1 * otherHunter[0]
	temp0 = temp1 + temp0
	temp1 = temp3 * otherHunter[0]
	if temp1 > otherHunter[0] :
		if otherHunter[0] != 0:
			temp0 = dist % otherHunter[0]
		else:
			temp0 = otherHunter[0]
	else:
		temp0 = min( temp0 , temp2 )
	if dist != 0:
		temp1 = temp2 % dist
	else:
		temp1 = dist
	temp4 = min( temp0 , temp1 )
	temp5 = min( temp3 , otherHunter[0] )
	temp2 = -1 * dist
	temp3 = min( temp2 , temp0 )
	if temp0 != 0:
		temp5 = temp5 % temp0
	else:
		temp5 = temp0
	temp5 = prey[1] - temp4
	temp2 = max( temp3 , temp1 )
	temp0 = temp5 - otherHunter[0]
	temp4 = temp1 * temp2
	return [ otherHunter[1] , temp2 ]
