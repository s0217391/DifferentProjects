#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	if temp0 > prey[0]:
		temp1 = -1 * prey[1]
	else:
		if temp0 != 0:
			temp1 = prey[1] / temp0
		else:
			temp1 = temp0
	temp0 = temp1 * prey[0]
	temp0 = min(temp0, prey[0])
	temp2 = min(temp0, prey[1])
	temp0 = temp2 - prey[1]
	temp0 = temp2 - prey[0]
	temp3 = -1 * temp0
	if temp1 != 0:
		temp1 = temp2 / temp1
	else:
		temp1 = temp1
	if temp1 != 0:
		temp4 = temp1 / temp1
	else:
		temp4 = temp1
	temp0 = temp3 + temp3
	if temp3 > prey[0]:
		temp3 = prey[0] * temp3
	else:
		if temp4 != 0:
			temp3 = prey[0] % temp4
		else:
			temp3 = temp4
	temp1 = max(temp1, prey[1])
	temp0 = -1 * temp0
	if prey[1] != 0:
		temp1 = temp1 / prey[1]
	else:
		temp1 = prey[1]
	if temp3 > temp3:
		temp4 = max(prey[0], temp2)
	else:
		temp4 = max(temp0, temp0)
	if temp3 != 0:
		temp1 = temp0 / temp3
	else:
		temp1 = temp3
	temp3 = -1 * prey[0]
	temp5 = temp3 * temp1
	return [temp4, temp4]
