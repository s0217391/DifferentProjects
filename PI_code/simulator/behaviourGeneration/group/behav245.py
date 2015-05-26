#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > prey[0] :
		temp0 = dist + dist
	else:
		if prey[1] != 0:
			temp0 = prey[0] / prey[1]
		else:
			temp0 = prey[1]
	temp1 = otherHunter[0] + temp0
	temp2 = min( dist , prey[0] )
	if otherHunter[1] > temp1 :
		temp2 = temp2 - temp1
	else:
		temp2 = -1 * otherHunter[0]
	temp0 = prey[0] - otherHunter[0]
	if otherHunter[1] > otherHunter[1] :
		temp0 = max( prey[0] , otherHunter[1] )
	else:
		if temp0 != 0:
			temp0 = otherHunter[0] / temp0
		else:
			temp0 = temp0
	temp3 = otherHunter[0] * temp2
	if otherHunter[1] != 0:
		temp0 = prey[0] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp2 = prey[0] - otherHunter[0]
	temp4 = max( temp0 , prey[0] )
	temp1 = temp4 - temp3
	if temp4 != 0:
		temp3 = prey[1] / temp4
	else:
		temp3 = temp4
	temp0 = min( otherHunter[1] , temp2 )
	temp4 = dist + otherHunter[0]
	temp4 = temp1 * otherHunter[1]
	if prey[0] != 0:
		temp0 = temp2 / prey[0]
	else:
		temp0 = prey[0]
	temp1 = temp2 - temp2
	temp3 = min( temp0 , temp2 )
	temp1 = temp2 * temp2
	temp2 = max( temp0 , temp0 )
	temp0 = temp2 - dist
	temp2 = temp2 * otherHunter[0]
	if temp1 > prey[0] :
		temp5 = -1 * temp2
	else:
		temp5 = dist - temp3
	temp0 = -1 * otherHunter[1]
	return [ prey[0] , temp5 ]
