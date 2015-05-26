#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * dist
	temp1 = -1 * temp0
	if otherHunter[0] != 0:
		temp0 = otherHunter[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if dist != 0:
		temp2 = prey[0] % dist
	else:
		temp2 = dist
	if otherHunter[0] > prey[0] :
		if temp0 > otherHunter[1] :
			temp3 = -1 * temp0
		else:
			temp3 = max( temp0 , otherHunter[0] )
	else:
		temp3 = temp2 * temp1
	temp3 = prey[0] + otherHunter[0]
	if temp3 != 0:
		temp4 = otherHunter[1] / temp3
	else:
		temp4 = temp3
	temp1 = prey[0] * temp4
	if prey[0] > prey[0] :
		temp0 = max( otherHunter[0] , temp2 )
	else:
		temp0 = min( temp0 , prey[0] )
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	temp1 = temp4 + temp0
	if temp2 != 0:
		temp5 = otherHunter[0] % temp2
	else:
		temp5 = temp2
	temp1 = temp3 + temp2
	if dist != 0:
		temp3 = dist % dist
	else:
		temp3 = dist
	if temp5 != 0:
		temp6 = temp5 / temp5
	else:
		temp6 = temp5
	if temp5 != 0:
		temp1 = temp6 / temp5
	else:
		temp1 = temp5
	if temp6 != 0:
		temp5 = otherHunter[0] / temp6
	else:
		temp5 = temp6
	if temp4 != 0:
		temp2 = temp6 / temp4
	else:
		temp2 = temp4
	temp7 = -1 * prey[0]
	temp7 = temp1 * temp0
	if dist > temp5 :
		if prey[0] != 0:
			temp5 = temp1 / prey[0]
		else:
			temp5 = prey[0]
	else:
		temp5 = temp4 * temp2
	temp1 = max( temp1 , temp3 )
	return [ temp6 , temp1 ]
