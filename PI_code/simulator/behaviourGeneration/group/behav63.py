#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist - prey[1]
	temp1 = min( prey[0] , temp0 )
	temp0 = otherHunter[0] - otherHunter[1]
	temp1 = otherHunter[1] - prey[0]
	temp1 = -1 * otherHunter[0]
	temp1 = -1 * otherHunter[0]
	if prey[1] != 0:
		temp1 = dist % prey[1]
	else:
		temp1 = prey[1]
	temp1 = temp1 + prey[0]
	if otherHunter[1] > otherHunter[0] :
		temp2 = min( otherHunter[0] , otherHunter[0] )
	else:
		if prey[0] > dist :
			temp2 = otherHunter[0] - prey[1]
		else:
			if otherHunter[0] != 0:
				temp2 = prey[1] / otherHunter[0]
			else:
				temp2 = otherHunter[0]
	temp3 = -1 * temp2
	if otherHunter[1] != 0:
		temp4 = temp3 / otherHunter[1]
	else:
		temp4 = otherHunter[1]
	temp5 = prey[1] * otherHunter[0]
	temp5 = prey[1] + temp3
	if otherHunter[1] != 0:
		temp0 = otherHunter[1] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if temp1 > temp0 :
		temp0 = -1 * otherHunter[0]
	else:
		temp0 = -1 * temp0
	if temp0 > otherHunter[1] :
		temp1 = max( prey[0] , temp3 )
	else:
		temp1 = prey[1] + temp2
	temp4 = -1 * temp1
	if temp5 != 0:
		temp3 = temp4 / temp5
	else:
		temp3 = temp5
	if temp3 != 0:
		temp4 = temp3 % temp3
	else:
		temp4 = temp3
	temp0 = temp2 - dist
	if temp5 != 0:
		temp1 = temp5 % temp5
	else:
		temp1 = temp5
	if temp0 > temp4 :
		if prey[1] != 0:
			temp2 = otherHunter[0] % prey[1]
		else:
			temp2 = prey[1]
	else:
		temp2 = temp4 + temp1
	temp0 = -1 * temp5
	temp2 = max( otherHunter[0] , otherHunter[1] )
	return [ temp0 , temp4 ]
