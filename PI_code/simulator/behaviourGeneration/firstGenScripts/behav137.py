#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	if temp0 != 0:
		temp1 = prey[0] / temp0
	else:
		temp1 = temp0
	temp0 = -1 * temp0
	if prey[0] > prey[1]:
		if temp1 != 0:
			temp1 = temp1 % temp1
		else:
			temp1 = temp1
	else:
		temp1 = -1 * prey[0]
	if temp0 > prey[1]:
		if temp0 != 0:
			temp0 = prey[0] / temp0
		else:
			temp0 = temp0
	else:
		temp0 = max(prey[0], temp0)
	temp2 = prey[0] - temp0
	temp3 = temp0 * prey[0]
	if prey[0] > temp3:
		temp1 = temp0 - temp0
	else:
		temp1 = min(temp1, temp2)
	if temp0 > temp2:
		if temp0 != 0:
			temp4 = temp1 / temp0
		else:
			temp4 = temp0
	else:
		temp4 = temp0 - temp1
	temp5 = temp2 * prey[1]
	temp2 = -1 * temp2
	temp5 = max(prey[0], prey[1])
	temp4 = temp0 + temp4
	temp3 = -1 * temp3
	if temp4 != 0:
		temp5 = temp0 % temp4
	else:
		temp5 = temp4
	if temp3 != 0:
		temp3 = temp0 / temp3
	else:
		temp3 = temp3
	return [prey[1], prey[1]]
