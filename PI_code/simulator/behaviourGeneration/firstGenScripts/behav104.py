#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	temp0 = prey[0] + temp1
	temp0 = temp0 - prey[0]
	temp2 = min(temp0, prey[0])
	if temp1 != 0:
		temp1 = prey[1] / temp1
	else:
		temp1 = temp1
	temp1 = temp0 - temp2
	temp2 = prey[1] * prey[0]
	temp0 = -1 * temp2
	temp2 = temp0 + temp2
	if temp0 != 0:
		temp3 = prey[1] % temp0
	else:
		temp3 = temp0
	temp4 = min(prey[0], prey[0])
	if temp1 > prey[1]:
		temp3 = min(temp2, temp1)
	else:
		temp3 = temp2 * temp2
	temp5 = max(temp0, prey[1])
	if temp2 > temp5:
		if temp0 != 0:
			temp2 = prey[0] % temp0
		else:
			temp2 = temp0
	else:
		temp2 = temp1 + temp3
	if temp3 > temp0:
		temp2 = temp0 * temp1
	else:
		if prey[1] > temp5:
			if temp4 != 0:
				temp2 = prey[0] % temp4
			else:
				temp2 = temp4
		else:
			temp2 = max(temp0, temp1)
	if prey[0] > temp4:
		temp4 = max(prey[0], temp2)
	else:
		if temp4 > temp0:
			temp4 = temp4 * temp4
		else:
			if prey[1] != 0:
				temp4 = temp3 / prey[1]
			else:
				temp4 = prey[1]
	if temp5 != 0:
		temp3 = temp0 % temp5
	else:
		temp3 = temp5
	if temp5 != 0:
		temp4 = temp4 % temp5
	else:
		temp4 = temp5
	temp0 = temp5 * temp4
	temp4 = prey[0] * temp1
	temp4 = temp1 * temp3
	temp2 = prey[0] * prey[0]
	temp4 = temp2 * temp1
	if prey[0] != 0:
		temp5 = temp4 % prey[0]
	else:
		temp5 = prey[0]
	return [temp5, temp4]
