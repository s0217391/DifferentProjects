#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = otherHunter[1] * dist
	temp1 = prey[0] - prey[1]
	temp2 = temp0 + otherHunter[0]
	temp0 = temp2 + dist
	temp3 = dist - prey[1]
	if prey[1] != 0:
		temp0 = otherHunter[1] % prey[1]
	else:
		temp0 = prey[1]
	if otherHunter[1] != 0:
		temp2 = temp1 / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp4 = -1 * otherHunter[1]
	if prey[1] != 0:
		temp2 = otherHunter[1] % prey[1]
	else:
		temp2 = prey[1]
	if prey[0] > dist :
		temp3 = max( dist , temp2 )
	else:
		temp3 = prey[0] + prey[1]
	temp1 = min( prey[0] , otherHunter[0] )
	temp1 = max( dist , prey[1] )
	return [ otherHunter[1] , temp2 ]
