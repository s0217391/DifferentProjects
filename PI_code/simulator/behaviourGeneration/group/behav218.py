#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] * prey[1]
	temp1 = dist * otherHunter[0]
	temp0 = otherHunter[1] + otherHunter[0]
	if prey[1] > temp1 :
		temp2 = temp0 - otherHunter[1]
	else:
		if otherHunter[0] != 0:
			temp2 = dist / otherHunter[0]
		else:
			temp2 = otherHunter[0]
	if temp2 > prey[1] :
		temp1 = otherHunter[1] + otherHunter[1]
	else:
		if temp2 != 0:
			temp1 = otherHunter[0] % temp2
		else:
			temp1 = temp2
	if temp1 != 0:
		temp0 = otherHunter[0] % temp1
	else:
		temp0 = temp1
	temp0 = prey[1] * temp1
	temp1 = min( prey[1] , temp2 )
	temp0 = temp1 * otherHunter[1]
	if dist != 0:
		temp2 = temp2 % dist
	else:
		temp2 = dist
	temp2 = otherHunter[0] - dist
	if otherHunter[1] > dist :
		temp2 = min( otherHunter[0] , temp0 )
	else:
		temp2 = otherHunter[1] * temp2
	temp3 = max( prey[1] , dist )
	temp3 = otherHunter[0] * prey[1]
	if temp2 != 0:
		temp1 = temp3 / temp2
	else:
		temp1 = temp2
	if prey[0] > prey[0] :
		if prey[1] != 0:
			temp0 = otherHunter[1] / prey[1]
		else:
			temp0 = prey[1]
	else:
		temp0 = -1 * temp0
	temp4 = temp2 * temp1
	temp0 = temp4 * prey[1]
	temp2 = -1 * temp3
	temp4 = max( temp3 , temp1 )
	temp1 = otherHunter[0] + dist
	temp0 = dist * temp0
	temp0 = temp1 + temp3
	temp1 = max( temp4 , temp0 )
	temp0 = max( otherHunter[0] , temp4 )
	return [ otherHunter[1] , temp3 ]
