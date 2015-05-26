#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[1] , prey[1] )
	temp1 = min( prey[0] , dist )
	temp1 = temp1 - prey[0]
	temp2 = -1 * otherHunter[1]
	temp0 = otherHunter[0] * temp0
	temp3 = temp1 + dist
	temp0 = min( prey[0] , prey[0] )
	if temp1 != 0:
		temp2 = prey[1] / temp1
	else:
		temp2 = temp1
	if temp2 != 0:
		temp0 = prey[0] / temp2
	else:
		temp0 = temp2
	if temp3 != 0:
		temp4 = otherHunter[0] / temp3
	else:
		temp4 = temp3
	temp3 = temp4 - temp3
	if otherHunter[1] != 0:
		temp4 = temp0 / otherHunter[1]
	else:
		temp4 = otherHunter[1]
	if dist > temp2 :
		temp2 = otherHunter[0] - prey[0]
	else:
		temp2 = max( dist , temp4 )
	temp0 = temp2 + temp1
	temp2 = temp3 * temp1
	temp3 = min( prey[0] , temp2 )
	if temp1 != 0:
		temp1 = temp1 / temp1
	else:
		temp1 = temp1
	if otherHunter[1] > otherHunter[0] :
		temp2 = otherHunter[0] - temp2
	else:
		temp2 = temp1 * temp1
	temp2 = min( dist , temp3 )
	return [ temp0 , temp2 ]
