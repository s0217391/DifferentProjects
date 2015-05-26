#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , prey[0] )
	if dist != 0:
		temp1 = prey[0] % dist
	else:
		temp1 = dist
	temp2 = otherHunter[1] * temp0
	temp3 = -1 * otherHunter[1]
	temp0 = temp2 + otherHunter[1]
	if prey[0] > dist :
		temp3 = otherHunter[0] * dist
	else:
		if dist > temp2 :
			if otherHunter[1] > temp1 :
				temp3 = -1 * temp2
			else:
				if dist != 0:
					temp3 = otherHunter[1] % dist
				else:
					temp3 = dist
		else:
			if otherHunter[1] != 0:
				temp3 = temp0 / otherHunter[1]
			else:
				temp3 = otherHunter[1]
	temp3 = prey[1] * temp0
	temp2 = temp2 * otherHunter[1]
	if temp1 > otherHunter[1] :
		temp3 = otherHunter[1] - temp1
	else:
		temp3 = min( temp1 , otherHunter[1] )
	temp4 = min( temp1 , temp1 )
	temp3 = -1 * temp2
	return [ temp4 , prey[0] ]
