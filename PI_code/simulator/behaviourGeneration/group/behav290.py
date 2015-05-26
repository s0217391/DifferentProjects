#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] * prey[0]
	if otherHunter[0] != 0:
		temp1 = otherHunter[0] / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if prey[1] != 0:
		temp1 = temp1 % prey[1]
	else:
		temp1 = prey[1]
	temp0 = prey[0] + temp1
	if dist > prey[1] :
		if otherHunter[0] > prey[0] :
			temp1 = -1 * temp1
		else:
			temp1 = prey[1] + prey[0]
	else:
		temp1 = dist - otherHunter[1]
	if otherHunter[1] > prey[0] :
		temp0 = min( prey[0] , temp0 )
	else:
		temp0 = prey[1] * temp1
	temp2 = otherHunter[0] - otherHunter[0]
	temp0 = max( prey[1] , prey[0] )
	if temp2 != 0:
		temp3 = dist / temp2
	else:
		temp3 = temp2
	temp0 = min( otherHunter[1] , dist )
	if temp2 > prey[0] :
		temp3 = temp2 + dist
	else:
		temp3 = min( dist , temp0 )
	if dist > prey[0] :
		if otherHunter[1] != 0:
			temp3 = temp3 / otherHunter[1]
		else:
			temp3 = otherHunter[1]
	else:
		temp3 = prey[0] * otherHunter[0]
	if temp2 > otherHunter[0] :
		temp2 = max( prey[0] , temp3 )
	else:
		if prey[0] != 0:
			temp2 = temp1 % prey[0]
		else:
			temp2 = prey[0]
	if otherHunter[1] != 0:
		temp3 = prey[0] / otherHunter[1]
	else:
		temp3 = otherHunter[1]
	if prey[1] != 0:
		temp1 = temp2 % prey[1]
	else:
		temp1 = prey[1]
	temp1 = temp3 - prey[1]
	temp3 = max( dist , dist )
	temp3 = -1 * otherHunter[0]
	if temp2 != 0:
		temp2 = temp2 % temp2
	else:
		temp2 = temp2
	temp1 = min( temp3 , prey[0] )
	if prey[1] != 0:
		temp0 = temp3 % prey[1]
	else:
		temp0 = prey[1]
	temp0 = prey[1] * prey[1]
	return [ temp3 , dist ]
