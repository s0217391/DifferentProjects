#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[1]:
		temp0 = max(prey[0], prey[0])
	else:
		if prey[0] > prey[1]:
			temp0 = prey[1] - prey[1]
		else:
			if prey[0] != 0:
				temp0 = prey[1] % prey[0]
			else:
				temp0 = prey[0]
	if prey[0] > prey[1]:
		temp1 = prey[1] * prey[1]
	else:
		temp1 = min(temp0, prey[1])
	if prey[0] > temp0:
		temp2 = temp0 * prey[0]
	else:
		temp2 = prey[1] - prey[1]
	temp0 = temp1 - temp1
	temp0 = prey[1] * temp1
	temp1 = temp1 - prey[0]
	temp1 = -1 * temp2
	if temp0 != 0:
		temp3 = temp1 % temp0
	else:
		temp3 = temp0
	temp2 = max(temp0, temp2)
	temp1 = max(prey[1], prey[0])
	temp2 = min(temp0, prey[1])
	if prey[1] > temp0:
		temp2 = prey[1] - prey[1]
	else:
		if temp3 != 0:
			temp2 = temp1 / temp3
		else:
			temp2 = temp3
	temp1 = min(temp2, prey[1])
	temp0 = max(prey[0], prey[0])
	temp3 = min(temp3, prey[1])
	if temp2 != 0:
		temp4 = temp0 / temp2
	else:
		temp4 = temp2
	temp2 = temp2 + prey[1]
	if prey[0] != 0:
		temp0 = temp1 / prey[0]
	else:
		temp0 = prey[0]
	if prey[0] != 0:
		temp5 = prey[0] / prey[0]
	else:
		temp5 = prey[0]
	temp4 = -1 * temp5
	if prey[1] != 0:
		temp3 = temp5 % prey[1]
	else:
		temp3 = prey[1]
	return [temp4, temp0]
