#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + otherHunter[0]
	if prey[1] != 0:
		temp1 = prey[1] / prey[1]
	else:
		temp1 = prey[1]
	temp2 = -1 * temp0
	if temp1 != 0:
		temp0 = dist % temp1
	else:
		temp0 = temp1
	if temp2 != 0:
		temp3 = otherHunter[0] / temp2
	else:
		temp3 = temp2
	temp2 = -1 * temp0
	temp3 = min( dist , temp2 )
	if temp1 != 0:
		temp4 = temp3 / temp1
	else:
		temp4 = temp1
	if temp0 > temp1 :
		if temp3 > temp0 :
			temp4 = prey[1] + temp3
		else:
			temp4 = temp0 - dist
	else:
		temp4 = otherHunter[0] * prey[1]
	temp0 = temp3 + temp1
	temp5 = temp2 * prey[1]
	if temp2 > otherHunter[0] :
		temp1 = -1 * dist
	else:
		temp1 = min( prey[0] , temp4 )
	temp1 = dist * otherHunter[1]
	temp4 = -1 * temp2
	if prey[0] > otherHunter[0] :
		if prey[0] != 0:
			temp3 = dist / prey[0]
		else:
			temp3 = prey[0]
	else:
		temp3 = temp4 * temp4
	if dist != 0:
		temp5 = temp0 % dist
	else:
		temp5 = dist
	if temp1 > prey[1] :
		if temp3 != 0:
			temp5 = prey[1] % temp3
		else:
			temp5 = temp3
	else:
		temp5 = max( prey[0] , temp4 )
	if temp3 != 0:
		temp5 = temp4 / temp3
	else:
		temp5 = temp3
	return [ temp0 , temp2 ]
