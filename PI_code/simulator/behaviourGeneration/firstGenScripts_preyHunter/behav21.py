#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * prey[1]
	temp0 = min(prey[0], temp1)
	temp1 = prey[1] - temp1
	if prey[0] > prey[0]:
		temp1 = temp0 + temp0
	else:
		temp1 = temp1 - prey[0]
	temp0 = prey[0] * temp0
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	temp1 = temp1 - temp1
	temp1 = min(temp0, prey[1])
	if temp1 > temp0:
		temp2 = temp1 * temp1
	else:
		temp2 = prey[1] + prey[0]
	if prey[1] != 0:
		temp0 = temp1 % prey[1]
	else:
		temp0 = prey[1]
	temp1 = prey[0] + prey[1]
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = min(prey[0], prey[1])
	if temp0 > prey[0]:
		if temp2 != 0:
			temp2 = prey[1] / temp2
		else:
			temp2 = temp2
	else:
		temp2 = min(temp1, prey[1])
	temp3 = min(prey[1], temp0)
	if temp3 != 0:
		temp0 = temp1 / temp3
	else:
		temp0 = temp3
	temp4 = max(temp2, prey[1])
	temp5 = temp2 + prey[0]
	if temp0 != 0:
		temp2 = prey[0] / temp0
	else:
		temp2 = temp0
	if temp4 > temp0:
		if prey[0] > temp0:
			if temp5 != 0:
				temp4 = prey[1] % temp5
			else:
				temp4 = temp5
		else:
			temp4 = prey[0] + prey[0]
	else:
		temp4 = prey[0] - prey[1]
	temp4 = min(prey[1], prey[1])
	temp2 = min(temp3, temp2)
	return [temp0, prey[0]]
