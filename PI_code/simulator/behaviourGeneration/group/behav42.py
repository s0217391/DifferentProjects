#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * dist
	temp1 = max( dist , dist )
	if prey[1] > temp0 :
		temp1 = temp0 - dist
	else:
		temp1 = temp0 + temp0
	temp2 = dist - prey[0]
	temp3 = prey[1] + dist
	if prey[1] > otherHunter[1] :
		if otherHunter[1] != 0:
			temp4 = prey[1] / otherHunter[1]
		else:
			temp4 = otherHunter[1]
	else:
		temp4 = max( otherHunter[1] , dist )
	if prey[1] != 0:
		temp5 = prey[0] / prey[1]
	else:
		temp5 = prey[1]
	if prey[1] > prey[1] :
		temp6 = -1 * temp3
	else:
		if temp4 != 0:
			temp6 = otherHunter[0] / temp4
		else:
			temp6 = temp4
	if dist != 0:
		temp3 = temp6 % dist
	else:
		temp3 = dist
	temp2 = otherHunter[1] - otherHunter[1]
	temp7 = min( temp4 , otherHunter[0] )
	return [ prey[0] , temp3 ]
