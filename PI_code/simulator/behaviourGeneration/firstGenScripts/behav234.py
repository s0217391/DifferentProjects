#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	if temp0 > prey[0]:
		if temp0 != 0:
			temp1 = prey[0] % temp0
		else:
			temp1 = temp0
	else:
		temp1 = max(temp0, prey[1])
	if temp1 != 0:
		temp0 = temp0 / temp1
	else:
		temp0 = temp1
	temp1 = temp1 + prey[0]
	temp0 = min(temp0, prey[0])
	if prey[1] > prey[0]:
		temp0 = temp1 + prey[1]
	else:
		temp0 = prey[0] + temp1
	temp1 = min(prey[1], temp0)
	if prey[0] > prey[0]:
		if prey[0] != 0:
			temp0 = prey[1] % prey[0]
		else:
			temp0 = prey[0]
	else:
		if temp0 != 0:
			temp0 = temp0 / temp0
		else:
			temp0 = temp0
	if prey[0] != 0:
		temp2 = temp0 / prey[0]
	else:
		temp2 = prey[0]
	if prey[1] != 0:
		temp3 = temp2 % prey[1]
	else:
		temp3 = prey[1]
	if temp0 > temp3:
		temp2 = -1 * temp0
	else:
		if temp2 != 0:
			temp2 = prey[1] % temp2
		else:
			temp2 = temp2
	if temp1 != 0:
		temp0 = temp0 / temp1
	else:
		temp0 = temp1
	temp1 = temp3 - prey[0]
	if prey[1] != 0:
		temp3 = temp1 / prey[1]
	else:
		temp3 = prey[1]
	if prey[0] > prey[1]:
		if temp3 > temp0:
			temp4 = -1 * temp0
		else:
			if temp3 != 0:
				temp4 = prey[1] % temp3
			else:
				temp4 = temp3
	else:
		temp4 = -1 * prey[0]
	temp5 = temp2 * temp0
	temp0 = min(temp0, temp0)
	if temp5 > temp5:
		if temp4 != 0:
			temp5 = temp0 / temp4
		else:
			temp5 = temp4
	else:
		if temp1 != 0:
			temp5 = prey[1] % temp1
		else:
			temp5 = temp1
	return [prey[0], temp1]
