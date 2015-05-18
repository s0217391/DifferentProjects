#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = min(prey[1], prey[0])
	temp2 = -1 * temp0
	if temp0 > temp2:
		temp2 = temp0 + temp1
	else:
		temp2 = temp0 * temp2
	if temp1 != 0:
		temp2 = prey[1] % temp1
	else:
		temp2 = temp1
	if prey[0] != 0:
		temp1 = prey[0] % prey[0]
	else:
		temp1 = prey[0]
	if temp1 != 0:
		temp1 = temp1 / temp1
	else:
		temp1 = temp1
	if temp0 > temp2:
		if temp0 != 0:
			temp1 = prey[1] % temp0
		else:
			temp1 = temp0
	else:
		temp1 = -1 * prey[1]
	if temp2 != 0:
		temp3 = temp0 % temp2
	else:
		temp3 = temp2
	if temp2 != 0:
		temp4 = prey[1] % temp2
	else:
		temp4 = temp2
	if temp1 != 0:
		temp4 = temp3 / temp1
	else:
		temp4 = temp1
	temp5 = min(prey[1], temp3)
	if temp4 != 0:
		temp3 = temp5 / temp4
	else:
		temp3 = temp4
	if temp5 != 0:
		temp6 = temp0 / temp5
	else:
		temp6 = temp5
	temp0 = -1 * prey[0]
	temp0 = min(prey[1], temp0)
	temp3 = temp3 + temp3
	temp1 = min(temp3, temp3)
	if temp1 > temp0:
		if temp5 != 0:
			temp7 = temp6 % temp5
		else:
			temp7 = temp5
	else:
		temp7 = -1 * temp1
	temp7 = temp3 * temp5
	temp6 = temp6 + temp2
	return [temp5, temp4]
