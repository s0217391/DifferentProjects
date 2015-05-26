#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist > dist :
		if dist != 0:
			temp0 = otherHunter[0] / dist
		else:
			temp0 = dist
	else:
		temp0 = prey[0] - otherHunter[0]
	if prey[0] != 0:
		temp1 = prey[0] % prey[0]
	else:
		temp1 = prey[0]
	if temp1 != 0:
		temp0 = prey[1] % temp1
	else:
		temp0 = temp1
	temp0 = otherHunter[0] + prey[0]
	temp0 = max( temp0 , otherHunter[1] )
	temp0 = -1 * otherHunter[1]
	if temp1 != 0:
		temp1 = temp1 % temp1
	else:
		temp1 = temp1
	temp0 = min( otherHunter[1] , dist )
	temp2 = otherHunter[1] + prey[1]
	if prey[1] != 0:
		temp0 = otherHunter[0] / prey[1]
	else:
		temp0 = prey[1]
	temp0 = otherHunter[0] - dist
	if prey[1] > prey[0] :
		temp1 = min( temp0 , otherHunter[1] )
	else:
		temp1 = -1 * prey[1]
	if prey[0] > prey[0] :
		temp0 = min( otherHunter[1] , prey[0] )
	else:
		temp0 = temp0 - temp0
	if dist != 0:
		temp2 = otherHunter[0] % dist
	else:
		temp2 = dist
	temp2 = temp2 - temp2
	temp2 = -1 * dist
	return [ temp2 , prey[1] ]
