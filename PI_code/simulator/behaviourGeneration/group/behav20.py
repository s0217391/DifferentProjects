#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] > dist :
		temp0 = prey[1] * prey[1]
	else:
		temp0 = otherHunter[0] * prey[1]
	temp1 = otherHunter[0] - prey[1]
	if prey[0] > temp0 :
		temp2 = min( otherHunter[0] , temp0 )
	else:
		if prey[1] > temp0 :
			if prey[0] > prey[0] :
				if otherHunter[1] != 0:
					temp2 = prey[0] % otherHunter[1]
				else:
					temp2 = otherHunter[1]
			else:
				temp2 = max( otherHunter[0] , temp1 )
		else:
			temp2 = -1 * prey[0]
	temp1 = otherHunter[0] - otherHunter[0]
	if otherHunter[0] != 0:
		temp1 = prey[0] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if prey[0] != 0:
		temp0 = dist % prey[0]
	else:
		temp0 = prey[0]
	temp2 = prey[1] + otherHunter[0]
	temp1 = max( dist , temp0 )
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	temp3 = -1 * dist
	temp4 = temp0 - prey[0]
	temp1 = otherHunter[1] - temp2
	temp3 = temp1 * temp2
	temp4 = prey[0] * dist
	temp5 = temp3 - temp4
	temp1 = max( otherHunter[1] , dist )
	temp5 = -1 * temp2
	temp3 = min( otherHunter[1] , dist )
	return [ dist , otherHunter[1] ]
