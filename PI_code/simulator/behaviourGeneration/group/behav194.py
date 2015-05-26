#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist > otherHunter[0] :
		temp0 = dist * dist
	else:
		temp0 = -1 * prey[1]
	if prey[1] > otherHunter[0] :
		if dist > prey[1] :
			temp1 = -1 * dist
		else:
			if otherHunter[1] != 0:
				temp1 = prey[0] / otherHunter[1]
			else:
				temp1 = otherHunter[1]
	else:
		temp1 = max( temp0 , dist )
	if prey[0] > prey[0] :
		if dist != 0:
			temp0 = temp1 / dist
		else:
			temp0 = dist
	else:
		temp0 = dist - temp1
	temp2 = min( otherHunter[1] , temp1 )
	temp3 = min( prey[1] , temp0 )
	temp1 = prey[1] - otherHunter[1]
	temp4 = max( temp2 , dist )
	if temp0 != 0:
		temp5 = temp3 / temp0
	else:
		temp5 = temp0
	temp2 = min( dist , temp2 )
	temp3 = dist + temp3
	temp4 = max( prey[0] , otherHunter[0] )
	if prey[0] != 0:
		temp3 = temp1 / prey[0]
	else:
		temp3 = prey[0]
	temp1 = dist * otherHunter[1]
	if temp2 > temp5 :
		temp2 = -1 * prey[1]
	else:
		if otherHunter[0] != 0:
			temp2 = temp1 / otherHunter[0]
		else:
			temp2 = otherHunter[0]
	temp2 = -1 * temp4
	return [ temp1 , prey[1] ]
