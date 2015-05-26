#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[1] , prey[0] )
	temp1 = max( otherHunter[1] , prey[1] )
	temp1 = otherHunter[0] * prey[0]
	temp1 = -1 * temp0
	temp0 = min( prey[1] , prey[1] )
	if temp0 != 0:
		temp1 = otherHunter[0] / temp0
	else:
		temp1 = temp0
	if temp0 > prey[0] :
		temp1 = min( prey[1] , temp1 )
	else:
		temp1 = temp0 * prey[1]
	temp1 = -1 * otherHunter[1]
	if prey[1] > temp1 :
		temp0 = prey[0] + temp1
	else:
		temp0 = -1 * otherHunter[0]
	temp0 = dist + temp0
	temp1 = otherHunter[1] * temp0
	if prey[1] > temp0 :
		temp1 = min( dist , dist )
	else:
		temp1 = -1 * dist
	temp1 = dist - temp0
	temp0 = temp1 - prey[1]
	return [ otherHunter[0] , prey[1] ]
