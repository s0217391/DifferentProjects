#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] - prey[0]
	temp1 = prey[0] + prey[0]
	temp0 = min( prey[0] , dist )
	if temp1 != 0:
		temp2 = temp1 / temp1
	else:
		temp2 = temp1
	temp1 = prey[1] - otherHunter[0]
	if dist != 0:
		temp2 = prey[0] / dist
	else:
		temp2 = dist
	if otherHunter[0] != 0:
		temp0 = otherHunter[1] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if prey[1] > dist :
		if otherHunter[0] > prey[0] :
			temp1 = min( prey[1] , prey[0] )
		else:
			if dist != 0:
				temp1 = otherHunter[0] % dist
			else:
				temp1 = dist
	else:
		if dist != 0:
			temp1 = temp1 % dist
		else:
			temp1 = dist
	temp3 = max( prey[0] , temp0 )
	if otherHunter[1] > prey[0] :
		temp4 = max( prey[1] , temp1 )
	else:
		temp4 = prey[0] - otherHunter[1]
	return [ temp0 , temp3 ]
