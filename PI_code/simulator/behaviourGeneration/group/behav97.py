#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	if dist > otherHunter[0] :
		temp1 = otherHunter[1] * otherHunter[0]
	else:
		temp1 = prey[1] + temp0
	temp2 = min( temp1 , otherHunter[1] )
	temp0 = temp2 + temp1
	temp2 = temp1 - temp2
	temp2 = temp1 * prey[1]
	if temp0 > temp2 :
		temp0 = min( dist , otherHunter[1] )
	else:
		temp0 = -1 * prey[1]
	temp2 = otherHunter[1] * prey[1]
	temp0 = -1 * otherHunter[1]
	if temp0 != 0:
		temp2 = temp0 % temp0
	else:
		temp2 = temp0
	temp0 = otherHunter[0] * prey[1]
	return [ temp0 , temp0 ]
