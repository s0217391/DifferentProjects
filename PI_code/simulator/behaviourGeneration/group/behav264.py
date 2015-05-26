#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist > otherHunter[1] :
		if prey[0] != 0:
			temp0 = otherHunter[1] % prey[0]
		else:
			temp0 = prey[0]
	else:
		temp0 = otherHunter[1] + prey[1]
	temp1 = -1 * otherHunter[0]
	if prey[0] != 0:
		temp1 = otherHunter[0] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = temp1 - temp0
	temp0 = temp2 * temp2
	if otherHunter[1] != 0:
		temp3 = temp0 % otherHunter[1]
	else:
		temp3 = otherHunter[1]
	temp4 = temp3 + temp3
	if temp1 != 0:
		temp3 = temp4 % temp1
	else:
		temp3 = temp1
	temp3 = temp0 - otherHunter[1]
	temp1 = -1 * temp2
	temp1 = dist * otherHunter[1]
	if temp2 > prey[1] :
		temp2 = dist - temp0
	else:
		temp2 = max( temp3 , temp3 )
	temp1 = dist - otherHunter[0]
	temp4 = dist * temp0
	temp4 = temp0 + temp3
	if otherHunter[0] != 0:
		temp0 = prey[1] / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp0 = min( prey[0] , temp1 )
	if temp2 != 0:
		temp5 = temp3 / temp2
	else:
		temp5 = temp2
	if dist != 0:
		temp5 = temp2 / dist
	else:
		temp5 = dist
	if prey[0] > temp0 :
		if temp0 > temp2 :
			temp4 = otherHunter[1] - otherHunter[1]
		else:
			temp4 = -1 * prey[1]
	else:
		temp4 = prey[0] + dist
	return [ otherHunter[0] , dist ]
