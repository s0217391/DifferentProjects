#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[0]:
		temp0 = min(prey[1], prey[0])
	else:
		if prey[0] > prey[1]:
			temp0 = min(prey[0], prey[0])
		else:
			if prey[0] != 0:
				temp0 = prey[0] % prey[0]
			else:
				temp0 = prey[0]
	temp1 = prey[1] * temp0
	temp0 = -1 * temp0
	if prey[0] != 0:
		temp2 = prey[1] / prey[0]
	else:
		temp2 = prey[0]
	if temp1 != 0:
		temp1 = prey[1] / temp1
	else:
		temp1 = temp1
	if prey[1] != 0:
		temp3 = temp1 % prey[1]
	else:
		temp3 = prey[1]
	if prey[0] != 0:
		temp4 = temp1 % prey[0]
	else:
		temp4 = prey[0]
	temp3 = temp2 * temp1
	temp1 = min(temp2, temp1)
	if temp4 > prey[1]:
		if temp3 > temp2:
			temp0 = max(temp3, temp3)
		else:
			temp0 = min(temp1, temp2)
	else:
		temp0 = temp0 + prey[0]
	if temp3 > prey[0]:
		temp1 = prey[0] + temp4
	else:
		temp1 = max(prey[1], prey[1])
	temp4 = temp3 - prey[0]
	temp3 = min(temp4, temp0)
	if temp4 != 0:
		temp2 = temp1 % temp4
	else:
		temp2 = temp4
	temp0 = temp0 - temp0
	if temp1 != 0:
		temp2 = temp4 % temp1
	else:
		temp2 = temp1
	temp1 = -1 * temp1
	temp3 = temp3 - prey[0]
	temp0 = max(prey[1], temp3)
	temp4 = min(temp0, temp3)
	temp4 = max(temp3, prey[0])
	temp5 = min(temp2, temp3)
	temp6 = -1 * prey[1]
	if temp3 != 0:
		temp6 = temp1 / temp3
	else:
		temp6 = temp3
	return [temp6, temp5]
