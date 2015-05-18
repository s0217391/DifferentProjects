#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[1])
	temp1 = prey[1] + temp0
	temp0 = min(prey[0], temp0)
	if prey[1] > prey[1]:
		if temp0 != 0:
			temp2 = prey[1] % temp0
		else:
			temp2 = temp0
	else:
		temp2 = -1 * prey[0]
	temp3 = temp1 * temp0
	if prey[1] != 0:
		temp2 = temp0 % prey[1]
	else:
		temp2 = prey[1]
	temp0 = -1 * temp2
	temp3 = min(temp2, temp2)
	if prey[0] != 0:
		temp0 = temp1 / prey[0]
	else:
		temp0 = prey[0]
	if temp1 > prey[0]:
		temp2 = temp3 + prey[0]
	else:
		temp2 = -1 * temp2
	temp2 = prey[0] * temp0
	if prey[1] > prey[0]:
		temp2 = -1 * prey[0]
	else:
		if temp1 != 0:
			temp2 = temp2 / temp1
		else:
			temp2 = temp1
	if temp3 != 0:
		temp1 = temp0 % temp3
	else:
		temp1 = temp3
	temp0 = prey[0] - temp3
	temp1 = temp1 + temp0
	if temp3 > temp2:
		if prey[1] != 0:
			temp4 = prey[0] % prey[1]
		else:
			temp4 = prey[1]
	else:
		temp4 = -1 * temp1
	if prey[0] != 0:
		temp1 = temp3 / prey[0]
	else:
		temp1 = prey[0]
	if prey[0] > temp1:
		if prey[0] != 0:
			temp3 = temp2 % prey[0]
		else:
			temp3 = prey[0]
	else:
		if temp2 != 0:
			temp3 = temp3 / temp2
		else:
			temp3 = temp2
	if temp1 > temp0:
		temp5 = temp3 * temp0
	else:
		temp5 = prey[1] * temp1
	if prey[1] > prey[0]:
		temp5 = temp2 * temp5
	else:
		temp5 = min(temp1, temp3)
	temp1 = max(prey[0], temp3)
	temp3 = prey[0] * temp3
	if temp0 > temp1:
		temp2 = max(temp3, temp3)
	else:
		temp2 = -1 * prey[1]
	temp3 = prey[1] - temp3
	return [temp3, temp1]
