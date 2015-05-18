#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		if prey[1] != 0:
			temp0 = prey[1] % prey[1]
		else:
			temp0 = prey[1]
	else:
		temp0 = max(prey[1], prey[0])
	if prey[1] > prey[1]:
		if temp0 != 0:
			temp1 = prey[0] % temp0
		else:
			temp1 = temp0
	else:
		temp1 = prey[1] - prey[0]
	if prey[0] > temp0:
		temp2 = -1 * temp0
	else:
		temp2 = -1 * prey[1]
	temp0 = min(prey[1], temp1)
	if prey[0] != 0:
		temp2 = prey[1] / prey[0]
	else:
		temp2 = prey[0]
	temp0 = max(temp1, temp0)
	temp2 = -1 * prey[0]
	temp3 = min(temp2, temp1)
	temp2 = temp3 - temp3
	if temp3 > temp2:
		temp4 = temp3 + prey[0]
	else:
		temp4 = prey[1] * prey[0]
	temp0 = temp1 + prey[0]
	if prey[1] != 0:
		temp2 = prey[0] % prey[1]
	else:
		temp2 = prey[1]
	temp3 = prey[1] - temp1
	temp0 = -1 * temp3
	temp1 = min(temp1, temp0)
	temp1 = -1 * prey[0]
	temp4 = temp2 + temp0
	temp5 = temp0 * temp2
	temp5 = temp5 + temp4
	if temp4 != 0:
		temp5 = prey[1] % temp4
	else:
		temp5 = temp4
	temp0 = temp3 * prey[1]
	temp5 = temp3 * prey[1]
	if prey[0] > temp4:
		temp5 = min(temp1, temp3)
	else:
		if prey[1] > temp2:
			if temp4 != 0:
				temp5 = temp1 / temp4
			else:
				temp5 = temp4
		else:
			temp5 = temp3 * temp2
	return [temp4, temp1]
