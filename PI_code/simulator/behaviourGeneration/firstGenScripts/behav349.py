#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = -1 * temp0
	temp0 = min(prey[1], temp0)
	temp0 = max(prey[1], temp0)
	if temp1 != 0:
		temp1 = temp0 / temp1
	else:
		temp1 = temp1
	if temp1 > prey[0]:
		if prey[0] != 0:
			temp1 = temp1 / prey[0]
		else:
			temp1 = prey[0]
	else:
		temp1 = prey[0] + temp0
	temp1 = max(temp0, prey[0])
	if temp1 > temp0:
		temp0 = temp1 + prey[1]
	else:
		if prey[1] > prey[1]:
			if prey[0] > temp0:
				temp0 = -1 * temp0
			else:
				if temp1 != 0:
					temp0 = prey[0] / temp1
				else:
					temp0 = temp1
		else:
			temp0 = prey[1] * prey[1]
	temp2 = max(prey[1], temp1)
	temp0 = temp1 * temp0
	if prey[1] != 0:
		temp2 = temp1 % prey[1]
	else:
		temp2 = prey[1]
	if temp2 != 0:
		temp2 = temp2 / temp2
	else:
		temp2 = temp2
	temp2 = temp2 - prey[0]
	temp1 = min(temp2, prey[0])
	temp1 = prey[1] + temp0
	if prey[0] != 0:
		temp3 = temp1 / prey[0]
	else:
		temp3 = prey[0]
	temp3 = min(prey[1], temp3)
	temp3 = prey[1] * prey[1]
	temp1 = -1 * temp0
	temp4 = -1 * temp1
	if prey[1] > prey[0]:
		temp1 = temp4 - temp3
	else:
		if temp0 != 0:
			temp1 = temp0 % temp0
		else:
			temp1 = temp0
	temp4 = max(temp3, temp0)
	if prey[0] != 0:
		temp2 = temp1 / prey[0]
	else:
		temp2 = prey[0]
	return [temp4, temp3]
