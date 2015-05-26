#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + otherHunter[0]
	temp1 = max( dist , temp0 )
	if temp0 != 0:
		temp1 = prey[0] / temp0
	else:
		temp1 = temp0
	if dist > dist :
		temp0 = otherHunter[0] * dist
	else:
		temp0 = temp1 + prey[0]
	temp2 = min( dist , prey[0] )
	temp2 = -1 * temp0
	temp1 = prey[0] - otherHunter[0]
	temp2 = prey[0] + temp0
	temp1 = prey[0] - otherHunter[1]
	temp3 = -1 * prey[0]
	if temp0 > temp2 :
		temp1 = otherHunter[1] - temp2
	else:
		temp1 = min( temp2 , prey[1] )
	if temp2 > temp3 :
		temp0 = prey[0] + temp3
	else:
		temp0 = prey[0] - dist
	if otherHunter[0] > temp0 :
		if temp0 != 0:
			temp0 = otherHunter[1] % temp0
		else:
			temp0 = temp0
	else:
		temp0 = max( temp1 , otherHunter[0] )
	if prey[0] != 0:
		temp3 = prey[1] % prey[0]
	else:
		temp3 = prey[0]
	temp3 = otherHunter[1] - temp0
	temp4 = dist * temp0
	if otherHunter[1] != 0:
		temp4 = prey[0] / otherHunter[1]
	else:
		temp4 = otherHunter[1]
	if temp1 != 0:
		temp3 = otherHunter[1] / temp1
	else:
		temp3 = temp1
	temp2 = dist * temp0
	if temp0 != 0:
		temp0 = prey[1] / temp0
	else:
		temp0 = temp0
	return [ otherHunter[0] , otherHunter[0] ]
