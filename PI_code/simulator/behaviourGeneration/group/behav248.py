#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] + dist
	temp1 = otherHunter[1] - prey[1]
	if otherHunter[0] > otherHunter[0] :
		temp1 = -1 * temp0
	else:
		temp1 = dist * prey[0]
	if dist != 0:
		temp2 = temp1 % dist
	else:
		temp2 = dist
	temp2 = min( prey[0] , prey[0] )
	temp0 = temp2 - temp1
	temp2 = temp1 - temp0
	if otherHunter[0] != 0:
		temp1 = otherHunter[0] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if prey[1] > dist :
		if otherHunter[0] != 0:
			temp2 = prey[1] / otherHunter[0]
		else:
			temp2 = otherHunter[0]
	else:
		temp2 = otherHunter[1] - dist
	temp1 = dist - prey[1]
	temp1 = min( temp0 , prey[1] )
	temp0 = prey[1] + temp1
	temp2 = temp1 - otherHunter[1]
	return [ otherHunter[1] , otherHunter[0] ]
