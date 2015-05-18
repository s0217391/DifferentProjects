#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	if temp0 > prey[0]:
		temp1 = min(prey[0], prey[0])
	else:
		if temp0 > temp0:
			temp1 = max(prey[1], prey[0])
		else:
			if prey[1] != 0:
				temp1 = prey[1] / prey[1]
			else:
				temp1 = prey[1]
	if prey[1] > prey[0]:
		temp1 = temp0 - temp1
	else:
		temp1 = prey[0] * temp1
	temp0 = max(temp0, temp0)
	temp0 = -1 * prey[0]
	if temp1 > prey[1]:
		temp0 = prey[0] + temp1
	else:
		temp0 = max(temp1, temp0)
	temp0 = prey[1] + temp1
	temp1 = -1 * prey[0]
	if temp1 != 0:
		temp2 = temp0 / temp1
	else:
		temp2 = temp1
	temp1 = prey[1] + prey[1]
	if temp0 != 0:
		temp1 = temp2 / temp0
	else:
		temp1 = temp0
	temp3 = -1 * prey[0]
	temp3 = min(temp1, prey[1])
	temp4 = prey[1] * temp2
	if prey[0] != 0:
		temp3 = temp4 % prey[0]
	else:
		temp3 = prey[0]
	temp4 = temp4 + temp2
	temp0 = temp1 + temp3
	temp5 = min(prey[0], prey[1])
	if temp2 > temp4:
		temp4 = min(temp2, prey[0])
	else:
		temp4 = max(prey[1], temp4)
	if temp3 > temp0:
		temp2 = temp5 - temp5
	else:
		if prey[0] != 0:
			temp2 = prey[1] % prey[0]
		else:
			temp2 = prey[0]
	if temp2 > prey[1]:
		temp4 = temp1 - prey[0]
	else:
		if temp2 > temp1:
			temp4 = max(temp2, temp1)
		else:
			temp4 = -1 * prey[1]
	temp6 = temp3 + temp5
	if prey[0] != 0:
		temp7 = temp2 / prey[0]
	else:
		temp7 = prey[0]
	temp7 = min(temp2, temp5)
	temp1 = -1 * temp2
	return [temp3, temp0]
