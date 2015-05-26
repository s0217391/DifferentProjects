#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , prey[1] )
	temp1 = prey[1] + prey[1]
	if prey[1] != 0:
		temp2 = temp1 / prey[1]
	else:
		temp2 = prey[1]
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp2 = min( prey[1] , prey[0] )
	temp0 = temp1 * otherHunter[1]
	temp0 = dist * prey[0]
	temp1 = temp1 + temp2
	if temp0 != 0:
		temp3 = otherHunter[0] % temp0
	else:
		temp3 = temp0
	temp1 = -1 * prey[0]
	temp3 = temp1 - temp1
	temp0 = temp2 + prey[1]
	if otherHunter[0] != 0:
		temp1 = prey[0] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp1 = otherHunter[1] + prey[0]
	temp2 = prey[0] * temp2
	if dist != 0:
		temp1 = otherHunter[0] % dist
	else:
		temp1 = dist
	if temp3 != 0:
		temp2 = dist / temp3
	else:
		temp2 = temp3
	temp3 = -1 * dist
	if temp0 > temp1 :
		temp1 = dist * temp0
	else:
		if prey[0] != 0:
			temp1 = dist / prey[0]
		else:
			temp1 = prey[0]
	temp1 = min( prey[0] , temp2 )
	if temp1 > temp1 :
		temp0 = max( temp3 , temp2 )
	else:
		if otherHunter[1] > prey[1] :
			if otherHunter[1] != 0:
				temp0 = otherHunter[0] / otherHunter[1]
			else:
				temp0 = otherHunter[1]
		else:
			temp0 = min( temp0 , prey[1] )
	temp0 = max( dist , temp0 )
	if temp0 > dist :
		temp2 = -1 * otherHunter[1]
	else:
		temp2 = otherHunter[1] * otherHunter[0]
	temp4 = -1 * otherHunter[0]
	temp3 = temp0 * temp2
	return [ temp3 , temp3 ]
