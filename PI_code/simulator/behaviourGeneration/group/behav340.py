#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[0]
	temp1 = max( prey[0] , otherHunter[0] )
	if temp1 > otherHunter[0] :
		temp0 = temp0 - otherHunter[0]
	else:
		if temp1 != 0:
			temp0 = prey[1] / temp1
		else:
			temp0 = temp1
	if prey[1] != 0:
		temp1 = prey[1] / prey[1]
	else:
		temp1 = prey[1]
	if temp0 > dist :
		temp2 = prey[1] - dist
	else:
		temp2 = prey[0] - temp1
	if otherHunter[1] > temp0 :
		if prey[1] != 0:
			temp1 = temp0 / prey[1]
		else:
			temp1 = prey[1]
	else:
		temp1 = min( prey[0] , otherHunter[0] )
	return [ temp2 , otherHunter[0] ]
