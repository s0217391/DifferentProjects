#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = prey[0] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = min( otherHunter[0] , prey[1] )
	temp2 = -1 * otherHunter[1]
	if otherHunter[1] > temp1 :
		temp2 = otherHunter[1] + temp1
	else:
		temp2 = otherHunter[1] * temp1
	if temp1 != 0:
		temp2 = otherHunter[0] % temp1
	else:
		temp2 = temp1
	if prey[0] != 0:
		temp1 = prey[1] % prey[0]
	else:
		temp1 = prey[0]
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	if dist > temp2 :
		if otherHunter[1] != 0:
			temp1 = otherHunter[0] % otherHunter[1]
		else:
			temp1 = otherHunter[1]
	else:
		temp1 = -1 * otherHunter[1]
	if temp1 != 0:
		temp3 = otherHunter[1] % temp1
	else:
		temp3 = temp1
	if temp1 != 0:
		temp4 = otherHunter[0] % temp1
	else:
		temp4 = temp1
	if dist != 0:
		temp4 = temp2 / dist
	else:
		temp4 = dist
	temp5 = min( otherHunter[0] , temp2 )
	if temp4 != 0:
		temp3 = temp5 / temp4
	else:
		temp3 = temp4
	if temp5 != 0:
		temp6 = otherHunter[1] / temp5
	else:
		temp6 = temp5
	temp0 = -1 * prey[0]
	temp0 = min( otherHunter[0] , otherHunter[1] )
	temp3 = temp2 + temp2
	temp1 = min( temp2 , temp1 )
	if dist > otherHunter[1] :
		if temp5 != 0:
			temp7 = temp6 % temp5
		else:
			temp7 = temp5
	else:
		temp7 = -1 * dist
	temp7 = temp2 * temp5
	temp6 = temp5 + temp0
	return [ temp5 , temp3 ]
