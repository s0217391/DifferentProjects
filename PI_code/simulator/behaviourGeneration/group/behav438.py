#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] + prey[0]
	if otherHunter[0] != 0:
		temp1 = prey[1] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if otherHunter[1] > temp0 :
		temp1 = otherHunter[1] - prey[0]
	else:
		temp1 = otherHunter[1] + temp1
	if dist != 0:
		temp2 = otherHunter[0] % dist
	else:
		temp2 = dist
	temp1 = otherHunter[0] - otherHunter[1]
	if prey[0] > temp0 :
		temp0 = temp0 - dist
	else:
		temp0 = max( otherHunter[0] , prey[1] )
	if otherHunter[1] > prey[0] :
		temp3 = -1 * temp2
	else:
		temp3 = dist + prey[0]
	temp1 = otherHunter[1] + temp1
	if temp0 > dist :
		temp0 = min( otherHunter[1] , temp3 )
	else:
		if otherHunter[1] != 0:
			temp0 = temp0 / otherHunter[1]
		else:
			temp0 = otherHunter[1]
	temp3 = prey[0] - otherHunter[0]
	if prey[0] != 0:
		temp0 = temp0 % prey[0]
	else:
		temp0 = prey[0]
	temp0 = -1 * prey[1]
	if prey[0] != 0:
		temp4 = prey[1] % prey[0]
	else:
		temp4 = prey[0]
	temp2 = temp4 - temp4
	temp3 = temp4 + temp0
	return [ prey[0] , prey[0] ]
