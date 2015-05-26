#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > dist :
		temp0 = min( prey[0] , prey[1] )
	else:
		temp0 = otherHunter[1] - prey[1]
	temp1 = prey[0] - temp0
	if dist != 0:
		temp1 = temp1 / dist
	else:
		temp1 = dist
	temp2 = prey[0] - temp1
	temp3 = dist + temp2
	temp1 = min( prey[1] , prey[1] )
	temp3 = min( prey[1] , otherHunter[1] )
	temp3 = max( temp0 , temp3 )
	if prey[0] > temp1 :
		if otherHunter[0] != 0:
			temp3 = otherHunter[1] % otherHunter[0]
		else:
			temp3 = otherHunter[0]
	else:
		temp3 = temp2 * temp3
	temp3 = prey[1] + prey[0]
	temp4 = max( temp1 , dist )
	temp3 = prey[0] - temp3
	temp0 = -1 * temp3
	if temp1 > prey[0] :
		temp0 = temp1 - otherHunter[1]
	else:
		if prey[1] != 0:
			temp0 = temp3 % prey[1]
		else:
			temp0 = prey[1]
	if prey[0] != 0:
		temp2 = temp3 % prey[0]
	else:
		temp2 = prey[0]
	temp0 = temp3 + otherHunter[0]
	temp0 = min( temp3 , prey[0] )
	if temp4 > prey[1] :
		temp5 = -1 * otherHunter[1]
	else:
		if otherHunter[1] != 0:
			temp5 = temp2 % otherHunter[1]
		else:
			temp5 = otherHunter[1]
	temp5 = -1 * temp0
	temp6 = min( temp5 , dist )
	return [ temp0 , prey[0] ]
