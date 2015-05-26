#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] - otherHunter[1]
	temp1 = temp0 + otherHunter[0]
	temp1 = otherHunter[0] * temp0
	temp0 = dist * prey[0]
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if temp1 > prey[1] :
		if prey[0] > dist :
			temp0 = temp1 + prey[0]
		else:
			if otherHunter[0] > dist :
				temp0 = temp0 + temp0
			else:
				temp0 = min( temp0 , dist )
	else:
		if temp0 > temp1 :
			if otherHunter[1] != 0:
				temp0 = otherHunter[1] / otherHunter[1]
			else:
				temp0 = otherHunter[1]
		else:
			if prey[1] != 0:
				temp0 = prey[0] / prey[1]
			else:
				temp0 = prey[1]
	temp0 = max( temp0 , dist )
	return [ otherHunter[1] , otherHunter[0] ]
