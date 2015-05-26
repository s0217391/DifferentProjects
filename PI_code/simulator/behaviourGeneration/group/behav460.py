#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = prey[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = min( prey[1] , dist )
	if otherHunter[1] != 0:
		temp1 = prey[0] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if prey[1] != 0:
		temp1 = otherHunter[1] / prey[1]
	else:
		temp1 = prey[1]
	if prey[1] > otherHunter[1] :
		temp0 = max( otherHunter[1] , otherHunter[1] )
	else:
		temp0 = otherHunter[0] + prey[0]
	temp1 = temp0 - dist
	temp0 = dist + dist
	temp2 = prey[1] + otherHunter[1]
	temp0 = min( otherHunter[1] , otherHunter[0] )
	temp2 = otherHunter[0] + prey[1]
	if prey[1] > temp2 :
		temp0 = temp0 * temp0
	else:
		if otherHunter[0] > temp0 :
			temp0 = temp2 + temp2
		else:
			temp0 = temp2 - temp2
	temp1 = max( temp1 , otherHunter[1] )
	temp2 = min( prey[0] , dist )
	temp1 = temp1 - otherHunter[1]
	temp0 = max( prey[1] , prey[0] )
	temp3 = prey[1] + temp2
	temp2 = -1 * otherHunter[0]
	if otherHunter[1] != 0:
		temp0 = temp0 % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp2 = temp2 * temp1
	temp4 = -1 * dist
	if temp3 != 0:
		temp1 = otherHunter[0] / temp3
	else:
		temp1 = temp3
	if prey[0] != 0:
		temp0 = dist / prey[0]
	else:
		temp0 = prey[0]
	temp2 = prey[1] - otherHunter[0]
	if dist != 0:
		temp1 = dist / dist
	else:
		temp1 = dist
	return [ dist , temp0 ]
