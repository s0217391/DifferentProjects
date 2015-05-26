#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = otherHunter[1] % dist
	else:
		temp0 = dist
	if dist > prey[0] :
		if dist != 0:
			temp1 = otherHunter[1] % dist
		else:
			temp1 = dist
	else:
		if prey[1] != 0:
			temp1 = otherHunter[1] / prey[1]
		else:
			temp1 = prey[1]
	temp2 = -1 * otherHunter[1]
	temp3 = temp0 - temp2
	temp2 = dist + prey[1]
	if prey[0] > otherHunter[0] :
		temp0 = temp3 - temp0
	else:
		temp0 = otherHunter[0] * otherHunter[1]
	temp1 = max( temp3 , prey[0] )
	temp1 = -1 * dist
	temp1 = temp0 + temp3
	temp3 = min( prey[1] , temp0 )
	temp2 = temp3 - prey[0]
	if dist != 0:
		temp3 = temp2 % dist
	else:
		temp3 = dist
	if prey[1] > otherHunter[1] :
		if dist > otherHunter[1] :
			temp0 = min( dist , temp0 )
		else:
			temp0 = temp3 + temp0
	else:
		temp0 = -1 * dist
	if prey[1] != 0:
		temp0 = temp2 % prey[1]
	else:
		temp0 = prey[1]
	temp2 = min( prey[0] , temp2 )
	return [ prey[0] , temp3 ]
