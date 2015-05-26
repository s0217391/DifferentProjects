#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist + prey[1]
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if prey[0] != 0:
		temp1 = prey[1] / prey[0]
	else:
		temp1 = prey[0]
	if otherHunter[0] != 0:
		temp0 = prey[0] / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if prey[1] != 0:
		temp0 = otherHunter[1] % prey[1]
	else:
		temp0 = prey[1]
	if temp1 != 0:
		temp2 = otherHunter[1] % temp1
	else:
		temp2 = temp1
	temp1 = min( dist , temp0 )
	temp2 = dist * otherHunter[0]
	temp0 = prey[0] * otherHunter[0]
	if otherHunter[1] > temp1 :
		temp2 = dist + prey[0]
	else:
		temp2 = min( prey[1] , otherHunter[0] )
	temp0 = min( dist , otherHunter[0] )
	temp0 = min( otherHunter[1] , otherHunter[1] )
	if dist != 0:
		temp3 = prey[0] % dist
	else:
		temp3 = dist
	temp0 = max( prey[1] , dist )
	if temp1 != 0:
		temp0 = dist / temp1
	else:
		temp0 = temp1
	temp1 = temp2 + prey[0]
	temp3 = otherHunter[0] - prey[0]
	if temp3 > temp1 :
		temp4 = max( prey[0] , prey[0] )
	else:
		temp4 = dist - otherHunter[0]
	temp5 = otherHunter[1] - prey[1]
	temp1 = max( prey[1] , temp1 )
	if temp1 > temp0 :
		if dist != 0:
			temp2 = temp1 % dist
		else:
			temp2 = dist
	else:
		temp2 = -1 * temp5
	return [ temp1 , prey[1] ]
