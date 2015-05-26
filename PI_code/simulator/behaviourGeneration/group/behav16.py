#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] + prey[0]
	if temp0 > prey[1] :
		temp1 = min( prey[1] , prey[1] )
	else:
		if dist > temp0 :
			temp1 = max( otherHunter[0] , prey[0] )
		else:
			if otherHunter[1] != 0:
				temp1 = otherHunter[1] / otherHunter[1]
			else:
				temp1 = otherHunter[1]
	if otherHunter[1] > prey[0] :
		temp1 = temp0 - temp1
	else:
		temp1 = prey[0] * temp1
	temp0 = max( otherHunter[1] , otherHunter[1] )
	temp0 = -1 * prey[1]
	if temp1 > otherHunter[1] :
		temp0 = prey[0] + temp0
	else:
		temp0 = max( temp0 , temp0 )
	temp0 = otherHunter[1] + temp1
	temp1 = -1 * prey[0]
	if temp0 != 0:
		temp2 = dist / temp0
	else:
		temp2 = temp0
	temp1 = otherHunter[1] + otherHunter[0]
	if dist != 0:
		temp1 = temp1 / dist
	else:
		temp1 = dist
	temp3 = -1 * prey[0]
	temp3 = min( dist , otherHunter[0] )
	temp4 = otherHunter[0] * temp1
	if prey[0] != 0:
		temp3 = temp3 % prey[0]
	else:
		temp3 = prey[0]
	temp4 = temp3 + temp0
	temp0 = dist + temp2
	temp5 = min( prey[0] , prey[1] )
	if temp1 > temp3 :
		temp4 = min( temp1 , prey[1] )
	else:
		temp4 = max( prey[1] , temp3 )
	if temp2 > otherHunter[0] :
		temp2 = temp5 - temp5
	else:
		if prey[1] != 0:
			temp2 = otherHunter[0] % prey[1]
		else:
			temp2 = prey[1]
	if temp0 > otherHunter[0] :
		temp4 = dist - prey[0]
	else:
		if temp1 > temp0 :
			temp4 = max( temp1 , dist )
		else:
			temp4 = -1 * otherHunter[0]
	temp6 = temp2 + temp4
	if prey[0] != 0:
		temp7 = temp0 / prey[0]
	else:
		temp7 = prey[0]
	temp7 = min( temp0 , temp4 )
	temp1 = -1 * temp1
	return [ temp2 , otherHunter[0] ]
