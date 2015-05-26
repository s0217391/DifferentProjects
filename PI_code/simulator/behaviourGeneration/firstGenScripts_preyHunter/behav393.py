#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	temp1 = temp0 - prey[0]
	if temp1 != 0:
		temp1 = temp0 / temp1
	else:
		temp1 = temp1
	temp0 = max(prey[1], prey[0])
	temp0 = temp0 - prey[0]
	if prey[0] > temp0:
		if temp1 != 0:
			temp2 = prey[0] % temp1
		else:
			temp2 = temp1
	else:
		temp2 = temp0 - prey[1]
	temp0 = max(prey[0], prey[0])
	temp3 = temp1 + temp2
	temp1 = min(temp0, temp2)
	temp2 = prey[1] - temp1
	temp4 = -1 * temp2
	if temp3 != 0:
		temp4 = temp4 % temp3
	else:
		temp4 = temp3
	if temp4 != 0:
		temp4 = prey[0] % temp4
	else:
		temp4 = temp4
	temp3 = temp1 * temp0
	temp1 = max(temp0, temp0)
	temp4 = temp4 + temp0
	if prey[1] != 0:
		temp5 = temp3 % prey[1]
	else:
		temp5 = prey[1]
	return [prey[0], temp5]
