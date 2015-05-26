#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[0]
	temp1 = min(prey[0], temp0)
	temp0 = prey[1] - temp0
	temp1 = temp0 - prey[0]
	temp1 = -1 * prey[1]
	temp1 = -1 * prey[1]
	if prey[0] != 0:
		temp1 = temp0 % prey[0]
	else:
		temp1 = prey[0]
	temp1 = temp1 + prey[0]
	if temp0 > prey[1]:
		temp2 = min(prey[1], prey[1])
	else:
		if prey[0] > temp0:
			temp2 = prey[1] - prey[0]
		else:
			if prey[1] != 0:
				temp2 = prey[1] / prey[1]
			else:
				temp2 = prey[1]
	temp3 = -1 * temp2
	if temp0 != 0:
		temp4 = temp3 / temp0
	else:
		temp4 = temp0
	temp5 = prey[1] * prey[1]
	temp5 = prey[1] + temp4
	if temp0 != 0:
		temp0 = temp0 % temp0
	else:
		temp0 = temp0
	if temp2 > temp1:
		temp0 = -1 * temp0
	else:
		temp0 = -1 * temp2
	if temp2 > temp0:
		temp1 = max(prey[0], temp4)
	else:
		temp1 = prey[1] + temp3
	temp4 = -1 * temp2
	if temp5 != 0:
		temp3 = temp5 / temp5
	else:
		temp3 = temp5
	if temp3 != 0:
		temp4 = temp4 % temp3
	else:
		temp4 = temp3
	temp0 = temp3 - temp1
	if temp5 != 0:
		temp1 = temp5 % temp5
	else:
		temp1 = temp5
	if temp2 > temp4:
		if prey[0] != 0:
			temp2 = prey[1] % prey[0]
		else:
			temp2 = prey[0]
	else:
		temp2 = temp4 + temp2
	temp0 = -1 * temp5
	temp2 = max(temp0, temp0)
	return [temp2, temp5]
