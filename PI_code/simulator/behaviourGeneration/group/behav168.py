#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] + dist
	if temp0 > otherHunter[0] :
		temp1 = -1 * dist
	else:
		temp1 = otherHunter[1] + dist
	temp0 = temp1 + prey[0]
	if dist != 0:
		temp0 = otherHunter[0] / dist
	else:
		temp0 = dist
	temp1 = max( dist , prey[1] )
	temp0 = min( dist , prey[0] )
	if otherHunter[1] > prey[1] :
		temp1 = prey[0] * otherHunter[0]
	else:
		if dist != 0:
			temp1 = temp1 / dist
		else:
			temp1 = dist
	if dist != 0:
		temp1 = prey[1] % dist
	else:
		temp1 = dist
	return [ prey[0] , dist ]
