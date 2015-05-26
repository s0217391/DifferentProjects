#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist > otherHunter[1] :
		temp0 = -1 * otherHunter[0]
	else:
		temp0 = max( otherHunter[0] , otherHunter[0] )
	if otherHunter[1] != 0:
		temp1 = temp0 / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if prey[0] != 0:
		temp2 = prey[0] % prey[0]
	else:
		temp2 = prey[0]
	if dist != 0:
		temp3 = prey[0] / dist
	else:
		temp3 = dist
	temp4 = min( temp1 , temp3 )
	temp4 = max( temp2 , otherHunter[1] )
	temp1 = temp1 + temp4
	if temp0 != 0:
		temp1 = temp2 % temp0
	else:
		temp1 = temp0
	if temp0 != 0:
		temp3 = otherHunter[1] % temp0
	else:
		temp3 = temp0
	if temp1 != 0:
		temp5 = temp4 / temp1
	else:
		temp5 = temp1
	temp2 = temp4 * temp2
	if otherHunter[0] != 0:
		temp0 = temp3 % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if otherHunter[1] > temp1 :
		temp0 = -1 * prey[1]
	else:
		if prey[0] != 0:
			temp0 = otherHunter[0] % prey[0]
		else:
			temp0 = prey[0]
	temp6 = min( temp3 , temp4 )
	if otherHunter[0] > temp0 :
		temp6 = temp2 + temp4
	else:
		if temp1 > dist :
			temp6 = prey[1] - temp6
		else:
			temp6 = temp6 - temp4
	if otherHunter[1] != 0:
		temp7 = temp6 % otherHunter[1]
	else:
		temp7 = otherHunter[1]
	temp1 = prey[1] + temp7
	temp0 = -1 * prey[1]
	if temp0 != 0:
		temp8 = temp4 % temp0
	else:
		temp8 = temp0
	temp9 = temp4 * temp5
	temp4 = max( temp6 , prey[0] )
	temp3 = -1 * otherHunter[0]
	temp2 = max( otherHunter[0] , temp3 )
	temp4 = max( temp3 , temp6 )
	if temp9 > temp8 :
		temp5 = -1 * temp9
	else:
		if otherHunter[1] != 0:
			temp5 = temp4 % otherHunter[1]
		else:
			temp5 = otherHunter[1]
	return [ prey[1] , temp9 ]
