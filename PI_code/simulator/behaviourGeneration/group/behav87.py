#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] + prey[1]
	temp1 = max( dist , prey[0] )
	temp2 = temp0 + otherHunter[1]
	temp0 = prey[0] + prey[1]
	temp1 = otherHunter[1] * temp2
	if temp1 != 0:
		temp3 = otherHunter[0] % temp1
	else:
		temp3 = temp1
	if temp1 != 0:
		temp2 = otherHunter[1] / temp1
	else:
		temp2 = temp1
	temp3 = temp3 - temp2
	temp4 = max( prey[0] , prey[1] )
	temp4 = -1 * temp4
	if temp4 > temp3 :
		temp3 = temp2 * temp3
	else:
		temp3 = temp0 * temp2
	if temp2 != 0:
		temp3 = prey[0] % temp2
	else:
		temp3 = temp2
	temp5 = otherHunter[0] * otherHunter[1]
	temp2 = otherHunter[1] - otherHunter[1]
	if prey[0] > prey[0] :
		temp2 = temp5 * temp3
	else:
		temp2 = temp2 * otherHunter[0]
	temp0 = temp1 + dist
	if dist != 0:
		temp5 = prey[0] % dist
	else:
		temp5 = dist
	temp0 = min( temp3 , otherHunter[1] )
	temp1 = prey[0] - temp3
	temp1 = -1 * prey[1]
	if prey[1] != 0:
		temp2 = temp0 / prey[1]
	else:
		temp2 = prey[1]
	return [ temp3 , temp5 ]
