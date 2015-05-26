#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] + otherHunter[0]
	temp1 = otherHunter[0] + dist
	temp2 = -1 * prey[1]
	if prey[0] != 0:
		temp3 = otherHunter[1] % prey[0]
	else:
		temp3 = prey[0]
	if prey[1] != 0:
		temp2 = temp0 % prey[1]
	else:
		temp2 = prey[1]
	if temp3 != 0:
		temp3 = dist / temp3
	else:
		temp3 = temp3
	temp1 = dist * dist
	if temp2 > temp2 :
		temp0 = -1 * temp1
	else:
		if otherHunter[1] != 0:
			temp0 = temp1 / otherHunter[1]
		else:
			temp0 = otherHunter[1]
	temp3 = -1 * otherHunter[0]
	temp0 = min( otherHunter[1] , prey[1] )
	if otherHunter[0] > prey[1] :
		temp4 = -1 * prey[1]
	else:
		if otherHunter[0] != 0:
			temp4 = prey[0] / otherHunter[0]
		else:
			temp4 = otherHunter[0]
	if otherHunter[1] != 0:
		temp3 = temp0 % otherHunter[1]
	else:
		temp3 = otherHunter[1]
	temp2 = temp4 * temp2
	temp4 = min( temp0 , temp4 )
	temp3 = temp1 * temp4
	if prey[0] > prey[1] :
		temp4 = temp1 * temp0
	else:
		if otherHunter[1] != 0:
			temp4 = dist / otherHunter[1]
		else:
			temp4 = otherHunter[1]
	temp4 = -1 * dist
	temp5 = temp0 - otherHunter[1]
	temp6 = max( otherHunter[0] , prey[0] )
	temp0 = temp5 - prey[1]
	return [ temp4 , temp2 ]
