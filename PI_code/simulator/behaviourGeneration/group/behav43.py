#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] + prey[1]
	temp1 = -1 * otherHunter[0]
	temp0 = dist - prey[0]
	temp1 = temp0 - temp0
	temp2 = min( temp1 , prey[0] )
	if temp1 > dist :
		temp0 = -1 * dist
	else:
		if temp1 > temp0 :
			temp0 = prey[1] + otherHunter[0]
		else:
			temp0 = otherHunter[0] + temp0
	temp0 = prey[1] * temp0
	temp2 = dist - temp2
	if prey[1] > otherHunter[0] :
		temp2 = otherHunter[0] * temp2
	else:
		if temp2 != 0:
			temp2 = otherHunter[0] / temp2
		else:
			temp2 = temp2
	if dist != 0:
		temp0 = otherHunter[1] / dist
	else:
		temp0 = dist
	temp0 = -1 * prey[0]
	temp0 = prey[0] + temp1
	temp1 = -1 * temp2
	temp3 = otherHunter[0] + temp0
	temp3 = temp2 - dist
	temp1 = max( temp3 , otherHunter[0] )
	if temp1 != 0:
		temp3 = temp2 / temp1
	else:
		temp3 = temp1
	return [ prey[0] , prey[0] ]
