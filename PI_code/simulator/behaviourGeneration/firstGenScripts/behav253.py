#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[1]
	temp1 = max(temp0, temp0)
	if temp1 != 0:
		temp1 = prey[0] / temp1
	else:
		temp1 = temp1
	if temp0 > temp0:
		temp0 = prey[1] * temp0
	else:
		temp0 = temp1 + prey[0]
	temp2 = min(temp0, prey[0])
	temp2 = -1 * temp1
	temp1 = prey[0] - prey[1]
	temp2 = prey[0] + temp1
	temp1 = prey[0] - temp0
	temp3 = -1 * prey[0]
	if temp1 > temp3:
		temp1 = temp0 - temp3
	else:
		temp1 = min(temp2, prey[0])
	if temp2 > temp3:
		temp0 = prey[0] + temp3
	else:
		temp0 = prey[0] - temp1
	if prey[1] > temp1:
		if temp1 != 0:
			temp0 = temp0 % temp1
		else:
			temp0 = temp1
	else:
		temp0 = max(temp2, prey[1])
	if prey[0] != 0:
		temp3 = prey[1] % prey[0]
	else:
		temp3 = prey[0]
	temp3 = temp0 - temp1
	temp4 = temp0 * temp1
	if temp0 != 0:
		temp4 = prey[0] / temp0
	else:
		temp4 = temp0
	if temp2 != 0:
		temp3 = temp0 / temp2
	else:
		temp3 = temp2
	temp2 = temp1 * temp1
	if temp2 != 0:
		temp0 = prey[0] / temp2
	else:
		temp0 = temp2
	return [prey[1], temp0]
