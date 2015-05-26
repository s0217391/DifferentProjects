#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[0] , dist )
	temp1 = prey[1] + temp0
	temp2 = temp0 * temp0
	if temp1 > temp1 :
		temp0 = max( prey[0] , otherHunter[1] )
	else:
		temp0 = min( otherHunter[0] , prey[0] )
	if temp0 > temp1 :
		if temp0 != 0:
			temp0 = otherHunter[0] / temp0
		else:
			temp0 = temp0
	else:
		if temp0 != 0:
			temp0 = prey[1] / temp0
		else:
			temp0 = temp0
	temp3 = prey[0] * otherHunter[1]
	if otherHunter[0] > otherHunter[1] :
		temp2 = -1 * temp2
	else:
		temp2 = min( prey[1] , prey[0] )
	temp3 = min( otherHunter[1] , temp0 )
	temp2 = prey[1] * dist
	if dist != 0:
		temp1 = temp2 % dist
	else:
		temp1 = dist
	return [ otherHunter[0] , prey[1] ]
