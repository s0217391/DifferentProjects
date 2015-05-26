#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[0] , otherHunter[0] )
	temp1 = min( dist , prey[0] )
	temp2 = min( temp1 , otherHunter[1] )
	temp0 = -1 * prey[1]
	if temp1 > dist :
		if otherHunter[1] > prey[1] :
			temp0 = -1 * prey[1]
		else:
			temp0 = min( prey[0] , prey[0] )
	else:
		temp0 = prey[0] - otherHunter[1]
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	temp2 = prey[0] - temp1
	temp3 = dist * otherHunter[1]
	temp0 = prey[0] - temp2
	if prey[0] != 0:
		temp3 = temp0 / prey[0]
	else:
		temp3 = prey[0]
	temp0 = min( dist , dist )
	if temp1 > temp2 :
		temp1 = prey[1] + otherHunter[0]
	else:
		if temp1 != 0:
			temp1 = temp0 % temp1
		else:
			temp1 = temp1
	if otherHunter[1] != 0:
		temp1 = prey[0] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if prey[0] != 0:
		temp3 = dist / prey[0]
	else:
		temp3 = prey[0]
	temp3 = -1 * prey[0]
	temp3 = -1 * temp3
	if temp1 != 0:
		temp3 = dist / temp1
	else:
		temp3 = temp1
	temp3 = temp0 + dist
	temp4 = -1 * prey[0]
	if temp2 != 0:
		temp3 = temp2 % temp2
	else:
		temp3 = temp2
	temp2 = temp2 - otherHunter[0]
	temp0 = max( dist , temp0 )
	temp4 = max( temp2 , prey[0] )
	if temp0 != 0:
		temp4 = prey[0] / temp0
	else:
		temp4 = temp0
	return [ temp4 , otherHunter[1] ]
