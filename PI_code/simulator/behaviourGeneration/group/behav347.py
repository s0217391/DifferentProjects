#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = otherHunter[0] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = -1 * prey[0]
	temp0 = -1 * prey[0]
	temp1 = dist + otherHunter[0]
	temp1 = dist * otherHunter[0]
	temp1 = temp0 + temp0
	temp0 = min( temp1 , prey[1] )
	temp1 = min( otherHunter[1] , temp1 )
	temp1 = otherHunter[1] - prey[1]
	if prey[0] != 0:
		temp1 = dist % prey[0]
	else:
		temp1 = prey[0]
	temp0 = max( prey[0] , temp0 )
	temp2 = otherHunter[1] * otherHunter[0]
	temp0 = min( prey[1] , dist )
	if temp0 > dist :
		if otherHunter[1] != 0:
			temp2 = temp2 / otherHunter[1]
		else:
			temp2 = otherHunter[1]
	else:
		temp2 = max( otherHunter[0] , temp1 )
	if temp0 > prey[0] :
		temp3 = max( prey[0] , temp2 )
	else:
		if prey[1] > prey[0] :
			if otherHunter[1] != 0:
				temp3 = prey[1] % otherHunter[1]
			else:
				temp3 = otherHunter[1]
		else:
			temp3 = prey[0] - otherHunter[0]
	return [ dist , dist ]
