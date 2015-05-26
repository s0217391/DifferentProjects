#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[1]
	temp1 = prey[0] + prey[1]
	temp2 = min(temp1, prey[0])
	temp1 = -1 * temp2
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp0 = temp2 * temp2
	temp0 = max(temp2, temp2)
	if temp0 > temp0:
		temp0 = prey[0] + temp1
	else:
		if temp0 > temp1:
			temp0 = max(prey[0], temp2)
		else:
			temp0 = prey[0] + temp1
	if temp2 != 0:
		temp0 = prey[0] % temp2
	else:
		temp0 = temp2
	temp0 = min(temp0, temp0)
	temp1 = temp2 - prey[1]
	if prey[0] > temp1:
		temp2 = -1 * prey[0]
	else:
		if prey[0] > temp2:
			temp2 = max(temp1, prey[1])
		else:
			temp2 = min(temp2, temp0)
	temp1 = max(temp1, temp1)
	if prey[0] != 0:
		temp3 = temp1 / prey[0]
	else:
		temp3 = prey[0]
	if temp0 > temp1:
		if temp2 != 0:
			temp3 = temp0 / temp2
		else:
			temp3 = temp2
	else:
		if temp1 != 0:
			temp3 = prey[0] / temp1
		else:
			temp3 = temp1
	if temp3 > prey[0]:
		temp4 = min(temp2, temp0)
	else:
		temp4 = prey[0] * temp0
	temp5 = temp2 + temp4
	if temp2 != 0:
		temp1 = temp4 / temp2
	else:
		temp1 = temp2
	if prey[0] > temp2:
		temp4 = min(temp3, temp1)
	else:
		temp4 = max(temp4, prey[1])
	temp2 = prey[1] - temp0
	temp1 = min(temp4, temp1)
	return [prey[0], temp2]
