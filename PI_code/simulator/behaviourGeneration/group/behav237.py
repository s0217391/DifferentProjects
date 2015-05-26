#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[0] , otherHunter[1] )
	temp1 = dist * dist
	temp2 = min( prey[1] , temp1 )
	temp1 = temp0 + temp1
	if otherHunter[0] > temp1 :
		temp1 = otherHunter[0] - temp2
	else:
		temp1 = max( temp0 , temp0 )
	temp0 = otherHunter[0] + temp0
	if temp0 > temp1 :
		temp3 = -1 * otherHunter[0]
	else:
		temp3 = temp2 - dist
	if dist != 0:
		temp3 = temp3 % dist
	else:
		temp3 = dist
	if otherHunter[1] > prey[1] :
		temp3 = -1 * temp0
	else:
		temp3 = min( temp1 , prey[1] )
	if prey[1] != 0:
		temp1 = prey[0] % prey[1]
	else:
		temp1 = prey[1]
	if prey[0] != 0:
		temp2 = temp0 % prey[0]
	else:
		temp2 = prey[0]
	if temp0 != 0:
		temp3 = otherHunter[1] / temp0
	else:
		temp3 = temp0
	if otherHunter[1] > prey[1] :
		if temp1 != 0:
			temp4 = prey[1] % temp1
		else:
			temp4 = temp1
	else:
		if otherHunter[0] > temp3 :
			temp4 = temp3 - dist
		else:
			temp4 = temp3 - prey[0]
	temp2 = otherHunter[1] - temp3
	temp5 = otherHunter[1] * prey[1]
	if temp2 != 0:
		temp2 = otherHunter[1] % temp2
	else:
		temp2 = temp2
	temp0 = max( otherHunter[0] , prey[0] )
	temp2 = max( temp5 , otherHunter[1] )
	return [ temp1 , otherHunter[0] ]
