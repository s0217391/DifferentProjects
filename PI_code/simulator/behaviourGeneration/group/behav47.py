#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( dist , otherHunter[0] )
	if prey[0] != 0:
		temp1 = prey[1] / prey[0]
	else:
		temp1 = prey[0]
	if temp1 > temp1 :
		temp2 = -1 * temp1
	else:
		temp2 = max( otherHunter[1] , temp0 )
	temp2 = otherHunter[0] + dist
	temp0 = min( otherHunter[0] , prey[1] )
	if prey[0] != 0:
		temp1 = dist % prey[0]
	else:
		temp1 = prey[0]
	if otherHunter[0] != 0:
		temp2 = dist % otherHunter[0]
	else:
		temp2 = otherHunter[0]
	if dist != 0:
		temp1 = dist % dist
	else:
		temp1 = dist
	temp0 = temp0 + prey[1]
	temp0 = temp0 * temp2
	if prey[0] != 0:
		temp0 = temp0 % prey[0]
	else:
		temp0 = prey[0]
	temp0 = min( temp1 , otherHunter[1] )
	temp2 = prey[0] - otherHunter[0]
	temp0 = -1 * otherHunter[0]
	if temp2 != 0:
		temp2 = prey[1] % temp2
	else:
		temp2 = temp2
	temp1 = otherHunter[0] * prey[1]
	temp3 = -1 * otherHunter[0]
	temp0 = -1 * dist
	if otherHunter[1] != 0:
		temp0 = temp3 % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp4 = prey[0] + temp0
	temp5 = temp2 - temp1
	temp0 = prey[0] * temp1
	temp4 = otherHunter[0] - prey[1]
	return [ otherHunter[1] , otherHunter[1] ]