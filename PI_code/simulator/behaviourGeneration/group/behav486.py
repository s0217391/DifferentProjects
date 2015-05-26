#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = dist % prey[1]
	else:
		temp0 = prey[1]
	if otherHunter[1] > otherHunter[1] :
		if otherHunter[0] > prey[1] :
			temp1 = otherHunter[1] + otherHunter[1]
		else:
			if otherHunter[0] != 0:
				temp1 = otherHunter[1] % otherHunter[0]
			else:
				temp1 = otherHunter[0]
	else:
		if prey[0] > dist :
			temp1 = temp0 - otherHunter[0]
		else:
			temp1 = -1 * prey[0]
	temp0 = max( dist , prey[1] )
	temp2 = -1 * temp0
	if prey[1] > prey[1] :
		if temp1 > dist :
			temp0 = min( dist , prey[1] )
		else:
			if otherHunter[0] != 0:
				temp0 = otherHunter[1] % otherHunter[0]
			else:
				temp0 = otherHunter[0]
	else:
		temp0 = otherHunter[1] - temp0
	if prey[0] != 0:
		temp3 = dist % prey[0]
	else:
		temp3 = prey[0]
	return [ dist , otherHunter[0] ]
