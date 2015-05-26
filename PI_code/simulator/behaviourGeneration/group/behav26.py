#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	if prey[0] > prey[1] :
		temp1 = dist * otherHunter[1]
	else:
		if dist > dist :
			temp1 = temp0 - otherHunter[0]
		else:
			if otherHunter[1] != 0:
				temp1 = prey[1] / otherHunter[1]
			else:
				temp1 = otherHunter[1]
	temp0 = max( otherHunter[1] , prey[0] )
	temp2 = otherHunter[0] + temp0
	temp2 = min( dist , prey[0] )
	temp3 = temp0 * otherHunter[1]
	temp2 = max( temp0 , prey[0] )
	temp0 = prey[1] + temp2
	temp0 = -1 * prey[1]
	if dist != 0:
		temp2 = dist / dist
	else:
		temp2 = dist
	if otherHunter[1] != 0:
		temp2 = prey[0] % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	return [ otherHunter[1] , temp1 ]
