#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		temp0 = max(prey[1], prey[0])
	else:
		if prey[1] > prey[1]:
			if prey[1] != 0:
				temp0 = prey[1] / prey[1]
			else:
				temp0 = prey[1]
		else:
			temp0 = min(prey[1], prey[0])
	temp1 = -1 * prey[1]
	temp2 = temp1 + prey[0]
	temp0 = min(prey[0], temp1)
	temp2 = temp1 + temp0
	temp0 = temp0 - prey[0]
	if temp2 != 0:
		temp2 = prey[0] % temp2
	else:
		temp2 = temp2
	temp3 = max(prey[1], temp1)
	temp1 = max(temp3, temp1)
	if temp0 > prey[1]:
		temp2 = temp0 * temp1
	else:
		temp2 = min(temp1, prey[1])
	temp4 = prey[1] + temp3
	temp1 = temp4 * temp4
	if prey[1] != 0:
		temp0 = temp1 / prey[1]
	else:
		temp0 = prey[1]
	temp1 = temp0 + temp2
	if temp3 != 0:
		temp1 = prey[0] / temp3
	else:
		temp1 = temp3
	if temp4 > temp0:
		temp5 = max(prey[1], prey[0])
	else:
		temp5 = prey[1] * prey[1]
	temp1 = max(temp2, prey[1])
	if temp3 > temp5:
		temp2 = min(prey[1], temp0)
	else:
		if temp5 != 0:
			temp2 = temp4 % temp5
		else:
			temp2 = temp5
	if temp0 != 0:
		temp4 = temp5 / temp0
	else:
		temp4 = temp0
	temp2 = min(prey[1], prey[0])
	if temp5 > prey[0]:
		temp3 = prey[0] + temp2
	else:
		if temp4 != 0:
			temp3 = temp0 / temp4
		else:
			temp3 = temp4
	temp2 = min(temp2, temp0)
	if prey[1] > temp4:
		if prey[0] != 0:
			temp4 = temp1 % prey[0]
		else:
			temp4 = prey[0]
	else:
		if temp5 > temp2:
			temp4 = min(temp4, temp2)
		else:
			temp4 = temp0 + temp3
	if prey[0] != 0:
		temp4 = temp1 / prey[0]
	else:
		temp4 = prey[0]
	return [temp4, temp3]
