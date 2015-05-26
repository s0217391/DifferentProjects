#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > prey[0] :
		if dist != 0:
			temp0 = otherHunter[1] / dist
		else:
			temp0 = dist
	else:
		temp0 = otherHunter[0] + prey[1]
	temp1 = prey[0] * dist
	temp0 = prey[0] + otherHunter[0]
	temp0 = otherHunter[0] * temp1
	temp1 = prey[0] + otherHunter[1]
	temp1 = otherHunter[1] + temp0
	temp2 = temp1 - otherHunter[0]
	if temp1 != 0:
		temp2 = temp2 / temp1
	else:
		temp2 = temp1
	temp3 = max( prey[1] , prey[1] )
	if prey[0] > otherHunter[1] :
		temp1 = -1 * prey[1]
	else:
		temp1 = temp2 - prey[0]
	if prey[0] != 0:
		temp4 = temp1 / prey[0]
	else:
		temp4 = prey[0]
	temp1 = temp0 + prey[1]
	temp5 = max( dist , dist )
	temp2 = -1 * temp0
	temp5 = temp5 * prey[1]
	temp1 = temp1 * otherHunter[0]
	temp1 = max( prey[1] , temp5 )
	if temp5 > temp4 :
		temp4 = max( temp2 , temp5 )
	else:
		if temp0 != 0:
			temp4 = temp2 / temp0
		else:
			temp4 = temp0
	temp5 = temp4 + dist
	if temp4 != 0:
		temp5 = dist / temp4
	else:
		temp5 = temp4
	if temp5 != 0:
		temp6 = temp0 % temp5
	else:
		temp6 = temp5
	temp4 = temp6 + temp4
	if dist > temp0 :
		if otherHunter[0] > temp5 :
			temp2 = otherHunter[1] - temp6
		else:
			if otherHunter[0] > prey[1] :
				if temp6 != 0:
					temp2 = temp4 % temp6
				else:
					temp2 = temp6
			else:
				temp2 = otherHunter[0] + otherHunter[1]
	else:
		temp2 = -1 * temp1
	if temp5 > temp3 :
		temp7 = max( temp4 , temp6 )
	else:
		temp7 = -1 * temp2
	temp7 = -1 * temp0
	return [ temp4 , temp6 ]
