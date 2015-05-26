#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( dist , otherHunter[1] )
	temp1 = min( otherHunter[0] , prey[0] )
	temp1 = min( otherHunter[1] , otherHunter[1] )
	temp2 = -1 * temp1
	temp2 = -1 * dist
	temp1 = -1 * dist
	if temp2 > temp2 :
		if dist != 0:
			temp0 = temp1 % dist
		else:
			temp0 = dist
	else:
		if dist != 0:
			temp0 = temp2 / dist
		else:
			temp0 = dist
	temp3 = -1 * prey[0]
	temp2 = dist * prey[1]
	if temp0 > prey[1] :
		temp3 = dist + otherHunter[0]
	else:
		if temp0 != 0:
			temp3 = temp0 / temp0
		else:
			temp3 = temp0
	temp1 = -1 * otherHunter[0]
	temp4 = min( temp2 , dist )
	if otherHunter[0] > temp3 :
		temp1 = temp4 * otherHunter[1]
	else:
		temp1 = dist - otherHunter[0]
	if dist > prey[1] :
		if temp0 != 0:
			temp4 = temp2 % temp0
		else:
			temp4 = temp0
	else:
		if temp2 > otherHunter[1] :
			temp4 = min( temp1 , temp3 )
		else:
			temp4 = temp2 * prey[0]
	temp4 = -1 * temp1
	temp3 = min( temp1 , temp3 )
	temp2 = max( dist , temp3 )
	temp1 = max( temp0 , prey[0] )
	if temp2 > dist :
		if dist != 0:
			temp1 = otherHunter[1] % dist
		else:
			temp1 = dist
	else:
		temp1 = -1 * temp1
	if dist != 0:
		temp2 = temp0 / dist
	else:
		temp2 = dist
	if prey[1] != 0:
		temp0 = temp4 % prey[1]
	else:
		temp0 = prey[1]
	if dist != 0:
		temp3 = otherHunter[0] % dist
	else:
		temp3 = dist
	temp2 = temp4 + temp1
	return [ otherHunter[0] , otherHunter[1] ]
