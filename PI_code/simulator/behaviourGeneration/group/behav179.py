#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[1]
	if dist != 0:
		temp1 = prey[1] % dist
	else:
		temp1 = dist
	if prey[1] > otherHunter[1] :
		temp2 = -1 * otherHunter[1]
	else:
		temp2 = min( dist , prey[0] )
	if temp0 != 0:
		temp1 = dist / temp0
	else:
		temp1 = temp0
	if otherHunter[0] != 0:
		temp1 = temp1 / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp0 = temp1 + temp0
	temp1 = max( temp0 , temp1 )
	temp3 = max( temp2 , dist )
	if otherHunter[0] != 0:
		temp3 = temp3 % otherHunter[0]
	else:
		temp3 = otherHunter[0]
	if dist != 0:
		temp2 = temp0 / dist
	else:
		temp2 = dist
	if prey[0] != 0:
		temp3 = temp3 % prey[0]
	else:
		temp3 = prey[0]
	if dist != 0:
		temp4 = temp0 / dist
	else:
		temp4 = dist
	temp4 = temp3 * otherHunter[1]
	temp4 = otherHunter[1] + dist
	temp5 = min( temp0 , temp4 )
	temp4 = otherHunter[0] + temp4
	temp3 = temp0 - temp5
	if otherHunter[0] != 0:
		temp2 = prey[1] / otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp6 = prey[1] + temp2
	temp2 = temp2 * dist
	if temp5 != 0:
		temp2 = temp0 / temp5
	else:
		temp2 = temp5
	if temp2 != 0:
		temp4 = temp4 / temp2
	else:
		temp4 = temp2
	temp0 = max( prey[1] , temp5 )
	temp4 = otherHunter[1] * dist
	return [ temp6 , temp5 ]
