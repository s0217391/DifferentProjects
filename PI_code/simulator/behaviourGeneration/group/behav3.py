#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[0]
	if dist > otherHunter[1] :
		if prey[0] != 0:
			temp1 = otherHunter[0] / prey[0]
		else:
			temp1 = prey[0]
	else:
		if temp0 != 0:
			temp1 = otherHunter[0] % temp0
		else:
			temp1 = temp0
	temp0 = otherHunter[0] + otherHunter[1]
	temp2 = max( prey[1] , otherHunter[0] )
	temp0 = max( temp0 , temp2 )
	if temp1 != 0:
		temp3 = otherHunter[0] % temp1
	else:
		temp3 = temp1
	temp4 = -1 * temp1
	temp4 = max( dist , temp0 )
	temp4 = min( temp3 , temp0 )
	if otherHunter[0] != 0:
		temp5 = temp1 % otherHunter[0]
	else:
		temp5 = otherHunter[0]
	temp1 = -1 * temp5
	temp2 = -1 * temp0
	if otherHunter[1] != 0:
		temp3 = temp0 / otherHunter[1]
	else:
		temp3 = otherHunter[1]
	if temp4 != 0:
		temp6 = temp4 / temp4
	else:
		temp6 = temp4
	if temp2 != 0:
		temp1 = otherHunter[0] % temp2
	else:
		temp1 = temp2
	temp7 = otherHunter[0] + temp5
	temp7 = min( prey[0] , otherHunter[0] )
	temp6 = prey[0] + prey[0]
	if otherHunter[0] > temp0 :
		temp2 = dist + prey[1]
	else:
		if prey[1] != 0:
			temp2 = prey[0] / prey[1]
		else:
			temp2 = prey[1]
	if temp6 != 0:
		temp4 = temp6 % temp6
	else:
		temp4 = temp6
	temp6 = max( temp3 , prey[1] )
	if temp2 > temp1 :
		temp4 = temp0 - otherHunter[1]
	else:
		temp4 = prey[0] + prey[1]
	temp1 = temp7 + temp1
	temp8 = temp3 * otherHunter[1]
	return [ temp4 , temp0 ]