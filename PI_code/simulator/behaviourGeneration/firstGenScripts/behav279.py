#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	temp1 = max(prey[1], prey[1])
	temp1 = prey[1] + temp1
	if temp0 > prey[0]:
		temp1 = prey[0] * prey[1]
	else:
		temp1 = max(temp0, prey[1])
	temp2 = min(prey[0], temp0)
	if prey[1] != 0:
		temp3 = temp1 / prey[1]
	else:
		temp3 = prey[1]
	temp1 = min(temp2, prey[1])
	temp3 = min(prey[0], temp2)
	if temp1 != 0:
		temp0 = temp3 / temp1
	else:
		temp0 = temp1
	temp0 = prey[0] * temp3
	temp0 = min(temp3, prey[1])
	temp1 = prey[0] * temp0
	temp0 = min(temp1, temp2)
	if prey[0] > temp0:
		temp3 = -1 * prey[1]
	else:
		temp3 = temp2 - temp2
	temp1 = max(prey[0], temp1)
	temp0 = prey[1] - temp1
	temp2 = temp3 - temp3
	temp3 = min(temp1, prey[1])
	if temp0 > temp3:
		temp2 = temp2 - temp1
	else:
		temp2 = temp3 - prey[0]
	if prey[1] != 0:
		temp0 = temp1 % prey[1]
	else:
		temp0 = prey[1]
	temp0 = temp1 - prey[1]
	if temp0 > temp0:
		if prey[1] != 0:
			temp0 = temp2 % prey[1]
		else:
			temp0 = prey[1]
	else:
		if temp2 > prey[1]:
			if temp1 != 0:
				temp0 = temp1 / temp1
			else:
				temp0 = temp1
		else:
			temp0 = -1 * temp1
	if temp0 != 0:
		temp0 = temp1 % temp0
	else:
		temp0 = temp0
	return [temp2, temp2]
