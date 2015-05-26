#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist + prey[0]
	temp1 = dist - dist
	if otherHunter[0] > otherHunter[1] :
		if dist > dist :
			temp0 = max( temp0 , temp1 )
		else:
			if temp0 != 0:
				temp0 = otherHunter[1] % temp0
			else:
				temp0 = temp0
	else:
		temp0 = max( temp0 , temp0 )
	temp1 = max( prey[1] , temp0 )
	if prey[1] > otherHunter[1] :
		if prey[0] != 0:
			temp2 = dist / prey[0]
		else:
			temp2 = prey[0]
	else:
		if otherHunter[0] != 0:
			temp2 = prey[1] / otherHunter[0]
		else:
			temp2 = otherHunter[0]
	temp2 = temp2 * dist
	temp3 = -1 * temp2
	if otherHunter[1] != 0:
		temp3 = prey[0] / otherHunter[1]
	else:
		temp3 = otherHunter[1]
	if temp3 != 0:
		temp0 = prey[1] % temp3
	else:
		temp0 = temp3
	temp4 = -1 * temp2
	temp4 = min( otherHunter[0] , temp1 )
	if dist != 0:
		temp1 = otherHunter[1] / dist
	else:
		temp1 = dist
	temp0 = max( temp2 , prey[0] )
	temp3 = -1 * dist
	temp2 = prey[0] - temp4
	temp1 = max( temp1 , temp3 )
	if prey[0] > prey[1] :
		temp0 = min( dist , temp1 )
	else:
		temp0 = -1 * prey[1]
	if temp3 != 0:
		temp0 = temp2 % temp3
	else:
		temp0 = temp3
	if temp4 > temp0 :
		temp0 = max( temp1 , otherHunter[1] )
	else:
		if prey[0] > temp3 :
			if dist != 0:
				temp0 = dist % dist
			else:
				temp0 = dist
		else:
			temp0 = otherHunter[1] + temp1
	temp0 = prey[1] * dist
	return [ temp1 , dist ]
