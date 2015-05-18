#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[0]
	temp1 = -1 * temp0
	temp0 = temp1 - prey[1]
	temp1 = max(prey[0], prey[0])
	if temp1 != 0:
		temp2 = prey[1] % temp1
	else:
		temp2 = temp1
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	if temp0 != 0:
		temp0 = prey[0] / temp0
	else:
		temp0 = temp0
	if temp1 > prey[1]:
		temp1 = temp1 + temp1
	else:
		if temp1 > temp0:
			if prey[0] != 0:
				temp1 = temp0 % prey[0]
			else:
				temp1 = prey[0]
		else:
			temp1 = temp0 + temp2
	temp2 = prey[0] - temp2
	temp1 = temp0 - temp0
	temp3 = temp2 * prey[1]
	temp2 = temp2 * temp1
	if temp0 != 0:
		temp0 = temp0 / temp0
	else:
		temp0 = temp0
	if prey[1] > temp0:
		if prey[0] != 0:
			temp1 = temp3 / prey[0]
		else:
			temp1 = prey[0]
	else:
		temp1 = max(prey[0], temp1)
	temp0 = temp2 + temp2
	if temp0 != 0:
		temp0 = temp2 % temp0
	else:
		temp0 = temp0
	temp0 = temp2 * prey[0]
	temp0 = temp2 * temp2
	if prey[0] != 0:
		temp2 = temp0 % prey[0]
	else:
		temp2 = prey[0]
	if temp1 > temp1:
		if temp1 > prey[0]:
			temp4 = max(temp3, temp3)
		else:
			temp4 = min(temp1, temp0)
	else:
		if temp3 != 0:
			temp4 = temp0 % temp3
		else:
			temp4 = temp3
	temp2 = temp4 * temp0
	temp1 = prey[0] + temp2
	temp3 = min(temp4, prey[1])
	if temp0 != 0:
		temp5 = temp2 % temp0
	else:
		temp5 = temp0
	return [temp5, temp0]
