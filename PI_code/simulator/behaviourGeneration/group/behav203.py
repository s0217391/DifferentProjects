#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = dist / prey[0]
	else:
		temp0 = prey[0]
	temp1 = min( prey[0] , prey[1] )
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp0 = max( dist , prey[1] )
	temp0 = max( prey[1] , temp1 )
	if prey[1] != 0:
		temp2 = temp1 % prey[1]
	else:
		temp2 = prey[1]
	temp0 = temp2 - temp1
	if otherHunter[0] != 0:
		temp1 = temp2 / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp0 = min( prey[1] , dist )
	temp2 = min( dist , otherHunter[0] )
	if temp2 != 0:
		temp3 = otherHunter[1] / temp2
	else:
		temp3 = temp2
	temp4 = temp1 + prey[1]
	temp5 = prey[1] * temp4
	temp3 = temp2 - prey[0]
	if prey[1] != 0:
		temp3 = prey[1] / prey[1]
	else:
		temp3 = prey[1]
	temp0 = prey[0] + temp5
	if otherHunter[0] != 0:
		temp1 = prey[0] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if temp3 != 0:
		temp3 = temp2 % temp3
	else:
		temp3 = temp3
	if dist != 0:
		temp3 = otherHunter[0] / dist
	else:
		temp3 = dist
	temp3 = temp0 + temp5
	return [ temp2 , dist ]
