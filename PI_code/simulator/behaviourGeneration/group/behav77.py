#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	temp1 = min( prey[1] , otherHunter[0] )
	if temp0 > dist :
		if temp1 != 0:
			temp0 = otherHunter[0] / temp1
		else:
			temp0 = temp1
	else:
		temp0 = max( dist , prey[0] )
	if dist != 0:
		temp1 = prey[0] % dist
	else:
		temp1 = dist
	temp2 = otherHunter[1] + temp0
	if otherHunter[1] != 0:
		temp3 = temp2 / otherHunter[1]
	else:
		temp3 = otherHunter[1]
	temp2 = max( temp1 , otherHunter[1] )
	if temp0 != 0:
		temp4 = prey[1] / temp0
	else:
		temp4 = temp0
	if prey[0] != 0:
		temp0 = otherHunter[1] / prey[0]
	else:
		temp0 = prey[0]
	if temp0 != 0:
		temp4 = prey[0] % temp0
	else:
		temp4 = temp0
	if temp1 > temp2 :
		temp1 = temp4 + prey[0]
	else:
		temp1 = temp1 * dist
	return [ dist , dist ]
