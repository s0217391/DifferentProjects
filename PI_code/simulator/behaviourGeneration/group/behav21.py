#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = otherHunter[1] % dist
	else:
		temp0 = dist
	temp1 = -1 * otherHunter[1]
	temp0 = min( prey[0] , temp1 )
	temp1 = otherHunter[0] - temp1
	if prey[0] > prey[0] :
		temp1 = dist + dist
	else:
		temp1 = temp1 - prey[0]
	temp0 = prey[0] * dist
	if prey[1] != 0:
		temp1 = otherHunter[1] / prey[1]
	else:
		temp1 = prey[1]
	temp1 = temp1 - temp1
	temp1 = min( dist , otherHunter[1] )
	if temp1 > dist :
		temp2 = temp0 * temp1
	else:
		temp2 = otherHunter[0] + prey[0]
	if otherHunter[0] != 0:
		temp0 = temp0 % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = prey[0] + prey[1]
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = min( prey[1] , otherHunter[0] )
	if otherHunter[1] > prey[1] :
		if temp1 != 0:
			temp2 = otherHunter[0] / temp1
		else:
			temp2 = temp1
	else:
		temp2 = min( temp0 , otherHunter[0] )
	temp3 = min( otherHunter[1] , otherHunter[1] )
	if temp3 != 0:
		temp0 = dist / temp3
	else:
		temp0 = temp3
	temp4 = max( temp1 , otherHunter[0] )
	temp5 = temp1 + prey[0]
	if otherHunter[1] != 0:
		temp2 = prey[0] / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	if temp4 > otherHunter[0] :
		if prey[1] > otherHunter[1] :
			if temp5 != 0:
				temp4 = otherHunter[0] % temp5
			else:
				temp4 = temp5
		else:
			temp4 = prey[0] + prey[1]
	else:
		temp4 = prey[0] - prey[1]
	temp4 = min( otherHunter[0] , otherHunter[0] )
	temp2 = min( temp2 , temp1 )
	return [ otherHunter[1] , prey[0] ]
