#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] - dist
	temp1 = min( temp0 , dist )
	if otherHunter[1] > prey[0] :
		temp1 = max( otherHunter[0] , dist )
	else:
		temp1 = dist - temp1
	if prey[1] != 0:
		temp2 = prey[0] % prey[1]
	else:
		temp2 = prey[1]
	temp2 = otherHunter[1] * otherHunter[0]
	if temp0 != 0:
		temp3 = otherHunter[1] / temp0
	else:
		temp3 = temp0
	temp1 = temp0 - temp0
	if otherHunter[0] > dist :
		if temp3 != 0:
			temp0 = prey[1] % temp3
		else:
			temp0 = temp3
	else:
		temp0 = max( prey[0] , prey[0] )
	temp4 = max( temp1 , dist )
	if prey[0] != 0:
		temp4 = temp4 / prey[0]
	else:
		temp4 = prey[0]
	temp5 = dist - otherHunter[0]
	if otherHunter[0] != 0:
		temp5 = temp1 % otherHunter[0]
	else:
		temp5 = otherHunter[0]
	temp5 = dist + temp3
	temp5 = max( dist , temp0 )
	if temp3 != 0:
		temp4 = prey[0] % temp3
	else:
		temp4 = temp3
	if temp3 > temp5 :
		temp0 = prey[0] - temp2
	else:
		if dist != 0:
			temp0 = temp3 % dist
		else:
			temp0 = dist
	return [ prey[0] , dist ]
