#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[1])
	temp1 = temp0 * temp0
	if prey[0] > temp1:
		temp0 = max(temp0, temp0)
	else:
		if prey[0] != 0:
			temp0 = temp1 % prey[0]
		else:
			temp0 = prey[0]
	if temp1 != 0:
		temp0 = prey[0] / temp1
	else:
		temp0 = temp1
	temp2 = max(prey[1], prey[1])
	if temp1 > temp1:
		temp2 = max(temp0, prey[1])
	else:
		temp2 = prey[1] - prey[1]
	temp0 = -1 * prey[0]
	if temp1 != 0:
		temp2 = temp0 / temp1
	else:
		temp2 = temp1
	if temp0 != 0:
		temp0 = temp2 / temp0
	else:
		temp0 = temp0
	temp1 = min(temp1, prey[1])
	temp3 = temp0 - prey[1]
	if temp1 != 0:
		temp4 = prey[0] % temp1
	else:
		temp4 = temp1
	temp1 = min(prey[0], temp4)
	if temp1 != 0:
		temp2 = prey[1] % temp1
	else:
		temp2 = temp1
	temp2 = temp4 - temp0
	temp0 = min(prey[0], prey[1])
	if temp3 > temp0:
		if temp3 != 0:
			temp0 = temp2 % temp3
		else:
			temp0 = temp3
	else:
		temp0 = -1 * temp2
	temp4 = temp0 - prey[0]
	temp5 = min(temp2, temp1)
	if prey[1] > prey[1]:
		temp6 = max(temp0, temp1)
	else:
		temp6 = temp5 * temp4
	temp3 = temp5 + prey[1]
	if prey[0] != 0:
		temp2 = temp5 / prey[0]
	else:
		temp2 = prey[0]
	if temp1 != 0:
		temp3 = temp6 / temp1
	else:
		temp3 = temp1
	temp2 = temp1 + temp5
	if temp0 > temp5:
		if temp5 > prey[1]:
			if temp1 > temp0:
				if temp4 != 0:
					temp4 = prey[1] / temp4
				else:
					temp4 = temp4
			else:
				temp4 = max(temp5, prey[1])
		else:
			temp4 = max(prey[0], prey[1])
	else:
		if temp2 > prey[1]:
			temp4 = min(temp0, temp0)
		else:
			temp4 = temp5 * temp0
	return [temp1, prey[0]]
