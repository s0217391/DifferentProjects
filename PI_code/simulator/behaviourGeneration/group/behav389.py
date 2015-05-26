#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( dist , prey[0] )
	temp1 = otherHunter[1] * otherHunter[0]
	temp0 = prey[0] - otherHunter[0]
	if otherHunter[0] > prey[1] :
		temp2 = temp1 - temp0
	else:
		temp2 = prey[0] * otherHunter[1]
	if temp1 != 0:
		temp0 = prey[0] / temp1
	else:
		temp0 = temp1
	temp1 = temp2 * otherHunter[0]
	temp1 = otherHunter[1] - temp0
	temp0 = min( prey[0] , temp1 )
	temp1 = min( otherHunter[1] , otherHunter[0] )
	temp0 = prey[0] + temp1
	temp1 = max( otherHunter[0] , temp2 )
	temp1 = min( dist , prey[0] )
	temp2 = otherHunter[1] * dist
	temp0 = otherHunter[0] * otherHunter[0]
	temp3 = temp2 + temp2
	if temp1 != 0:
		temp1 = prey[0] / temp1
	else:
		temp1 = temp1
	temp0 = max( otherHunter[1] , temp1 )
	temp3 = temp3 - prey[0]
	if dist != 0:
		temp2 = temp3 / dist
	else:
		temp2 = dist
	temp0 = prey[0] + dist
	temp0 = max( prey[1] , dist )
	return [ otherHunter[1] , temp3 ]
