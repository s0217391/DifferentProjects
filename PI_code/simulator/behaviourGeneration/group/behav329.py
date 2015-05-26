#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = otherHunter[1] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if prey[1] > temp0 :
		temp1 = -1 * dist
	else:
		temp1 = prey[0] * temp0
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	temp1 = dist + otherHunter[0]
	if dist != 0:
		temp1 = prey[1] % dist
	else:
		temp1 = dist
	temp1 = otherHunter[1] - otherHunter[1]
	temp0 = temp1 + prey[1]
	if temp0 > temp1 :
		temp0 = otherHunter[1] * temp1
	else:
		temp0 = -1 * prey[1]
	if temp0 > prey[1] :
		temp2 = otherHunter[1] + dist
	else:
		if prey[0] != 0:
			temp2 = temp0 / prey[0]
		else:
			temp2 = prey[0]
	temp1 = -1 * prey[0]
	if temp2 != 0:
		temp1 = temp2 % temp2
	else:
		temp1 = temp2
	if otherHunter[1] > prey[0] :
		if prey[0] > prey[1] :
			if temp2 != 0:
				temp1 = temp0 % temp2
			else:
				temp1 = temp2
		else:
			if dist != 0:
				temp1 = temp1 % dist
			else:
				temp1 = dist
	else:
		temp1 = temp0 - dist
	temp1 = -1 * otherHunter[1]
	temp0 = otherHunter[0] - temp0
	if temp0 != 0:
		temp1 = otherHunter[0] % temp0
	else:
		temp1 = temp0
	if otherHunter[1] > dist :
		temp0 = min( prey[0] , temp0 )
	else:
		temp0 = prey[1] + temp2
	temp0 = dist * temp0
	return [ otherHunter[0] , otherHunter[0] ]
