#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * prey[0]
	temp1 = min( prey[0] , prey[0] )
	temp1 = max( prey[1] , otherHunter[1] )
	temp1 = -1 * prey[0]
	temp0 = prey[0] + dist
	temp0 = otherHunter[1] - temp0
	if temp1 != 0:
		temp2 = temp1 / temp1
	else:
		temp2 = temp1
	temp1 = max( dist , prey[1] )
	temp1 = temp0 + temp0
	if prey[0] > temp2 :
		if otherHunter[1] > otherHunter[1] :
			temp1 = max( prey[0] , temp0 )
		else:
			temp1 = prey[1] + prey[1]
	else:
		if prey[1] > prey[0] :
			temp1 = prey[0] + temp1
		else:
			if otherHunter[1] > prey[1] :
				temp1 = max( otherHunter[1] , prey[0] )
			else:
				if temp0 != 0:
					temp1 = otherHunter[0] % temp0
				else:
					temp1 = temp0
	temp2 = max( otherHunter[1] , prey[1] )
	temp2 = dist + prey[0]
	temp0 = prey[0] - dist
	temp2 = prey[0] * temp0
	if prey[0] != 0:
		temp0 = temp2 % prey[0]
	else:
		temp0 = prey[0]
	if otherHunter[1] != 0:
		temp0 = dist % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if temp1 > otherHunter[1] :
		if dist != 0:
			temp3 = temp2 % dist
		else:
			temp3 = dist
	else:
		if otherHunter[0] != 0:
			temp3 = otherHunter[0] / otherHunter[0]
		else:
			temp3 = otherHunter[0]
	if prey[0] != 0:
		temp3 = prey[0] / prey[0]
	else:
		temp3 = prey[0]
	if temp0 > prey[1] :
		if otherHunter[1] != 0:
			temp4 = otherHunter[1] % otherHunter[1]
		else:
			temp4 = otherHunter[1]
	else:
		temp4 = min( otherHunter[1] , temp3 )
	if temp3 != 0:
		temp3 = temp2 / temp3
	else:
		temp3 = temp3
	return [ dist , temp4 ]
