#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > otherHunter[1] :
		temp0 = max( prey[1] , prey[1] )
	else:
		if otherHunter[0] > otherHunter[1] :
			temp0 = dist - dist
		else:
			if prey[1] != 0:
				temp0 = dist % prey[1]
			else:
				temp0 = prey[1]
	if prey[0] > otherHunter[1] :
		temp1 = otherHunter[1] * otherHunter[1]
	else:
		temp1 = min( temp0 , otherHunter[1] )
	if prey[0] > dist :
		temp2 = otherHunter[1] * prey[0]
	else:
		temp2 = otherHunter[1] - otherHunter[0]
	temp0 = temp1 - temp0
	temp0 = otherHunter[1] * dist
	temp1 = temp0 - prey[0]
	temp1 = -1 * temp2
	if otherHunter[1] != 0:
		temp3 = temp1 % otherHunter[1]
	else:
		temp3 = otherHunter[1]
	temp2 = max( otherHunter[1] , temp1 )
	temp1 = max( prey[1] , prey[1] )
	temp2 = min( dist , otherHunter[0] )
	if otherHunter[0] > dist :
		temp2 = otherHunter[0] - otherHunter[0]
	else:
		if temp3 != 0:
			temp2 = temp0 / temp3
		else:
			temp2 = temp3
	temp1 = min( temp2 , otherHunter[0] )
	temp0 = max( prey[0] , prey[1] )
	temp3 = min( temp2 , prey[1] )
	if temp2 != 0:
		temp4 = dist / temp2
	else:
		temp4 = temp2
	temp2 = temp1 + prey[1]
	if prey[1] != 0:
		temp0 = dist / prey[1]
	else:
		temp0 = prey[1]
	if prey[1] != 0:
		temp5 = prey[0] / prey[1]
	else:
		temp5 = prey[1]
	temp4 = -1 * temp4
	if prey[1] != 0:
		temp3 = temp4 % prey[1]
	else:
		temp3 = prey[1]
	return [ temp3 , otherHunter[1] ]
