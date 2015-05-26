#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] > dist :
		temp0 = prey[0] * otherHunter[0]
	else:
		temp0 = -1 * otherHunter[0]
	temp1 = prey[0] * prey[1]
	if dist != 0:
		temp1 = temp1 / dist
	else:
		temp1 = dist
	if otherHunter[0] > temp0 :
		if temp1 != 0:
			temp0 = temp1 / temp1
		else:
			temp0 = temp1
	else:
		temp0 = min( temp1 , prey[0] )
	temp2 = -1 * otherHunter[1]
	return [ temp2 , temp2 ]
