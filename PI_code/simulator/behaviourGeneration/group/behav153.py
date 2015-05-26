#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( dist , otherHunter[1] )
	temp1 = -1 * prey[0]
	if prey[1] != 0:
		temp2 = temp0 / prey[1]
	else:
		temp2 = prey[1]
	temp1 = max( otherHunter[0] , otherHunter[0] )
	temp1 = -1 * temp0
	if prey[0] > prey[0] :
		temp1 = temp1 - otherHunter[0]
	else:
		temp1 = otherHunter[1] - prey[1]
	if temp0 != 0:
		temp2 = temp2 % temp0
	else:
		temp2 = temp0
	temp0 = -1 * temp1
	temp0 = dist * temp2
	temp3 = -1 * otherHunter[0]
	if temp3 != 0:
		temp0 = prey[1] / temp3
	else:
		temp0 = temp3
	if temp0 > dist :
		temp4 = otherHunter[0] - prey[0]
	else:
		temp4 = min( dist , prey[0] )
	temp2 = max( temp4 , temp3 )
	temp2 = temp4 + otherHunter[0]
	temp5 = temp0 + temp2
	if temp3 > temp0 :
		temp1 = dist - temp3
	else:
		if prey[1] != 0:
			temp1 = temp5 / prey[1]
		else:
			temp1 = prey[1]
	temp1 = -1 * temp3
	if prey[1] != 0:
		temp4 = temp1 / prey[1]
	else:
		temp4 = prey[1]
	temp0 = min( otherHunter[1] , temp4 )
	if dist > temp1 :
		if prey[0] != 0:
			temp4 = temp0 / prey[0]
		else:
			temp4 = prey[0]
	else:
		if otherHunter[1] != 0:
			temp4 = temp0 % otherHunter[1]
		else:
			temp4 = otherHunter[1]
	if otherHunter[0] != 0:
		temp2 = prey[0] % otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp4 = temp1 - temp2
	temp4 = dist - otherHunter[0]
	if temp2 != 0:
		temp3 = temp5 % temp2
	else:
		temp3 = temp2
	temp2 = -1 * dist
	return [ temp0 , otherHunter[1] ]
