#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = prey[1] - prey[0]
	temp2 = min(temp0, temp1)
	temp1 = prey[0] - temp2
	if temp2 != 0:
		temp2 = prey[1] % temp2
	else:
		temp2 = temp2
	if temp2 > temp2:
		temp3 = prey[0] + temp0
	else:
		if temp0 != 0:
			temp3 = temp0 % temp0
		else:
			temp3 = temp0
	temp2 = temp3 + prey[1]
	temp3 = -1 * prey[1]
	temp3 = max(prey[0], temp2)
	temp1 = temp3 - temp0
	temp1 = min(temp1, temp2)
	temp3 = prey[0] * temp2
	temp2 = temp2 + temp1
	temp0 = prey[1] * prey[0]
	temp3 = min(temp1, temp2)
	temp0 = temp2 - temp3
	temp0 = temp0 - prey[1]
	if temp2 != 0:
		temp4 = temp0 % temp2
	else:
		temp4 = temp2
	if temp0 != 0:
		temp5 = temp0 / temp0
	else:
		temp5 = temp0
	if temp0 > temp5:
		temp4 = temp5 + prey[1]
	else:
		temp4 = prey[1] * prey[0]
	temp5 = temp4 + temp0
	temp0 = temp5 * temp3
	temp0 = temp2 * temp4
	temp6 = min(temp4, prey[1])
	if temp2 != 0:
		temp4 = temp3 % temp2
	else:
		temp4 = temp2
	return [temp0, prey[0]]
