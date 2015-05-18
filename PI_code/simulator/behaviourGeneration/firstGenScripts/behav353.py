#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[1]
	temp1 = max(prey[0], prey[0])
	temp0 = prey[0] - prey[1]
	temp0 = prey[0] - temp1
	temp2 = -1 * prey[1]
	if prey[1] != 0:
		temp3 = prey[1] / prey[1]
	else:
		temp3 = prey[1]
	temp3 = prey[0] * temp3
	temp1 = temp3 + temp0
	temp3 = min(temp3, prey[1])
	temp4 = -1 * temp1
	if prey[0] > temp4:
		if prey[1] != 0:
			temp4 = temp3 % prey[1]
		else:
			temp4 = prey[1]
	else:
		temp4 = min(temp3, temp4)
	temp0 = temp1 - prey[1]
	if temp4 != 0:
		temp2 = temp2 / temp4
	else:
		temp2 = temp4
	if temp2 > temp1:
		if temp1 != 0:
			temp1 = temp1 % temp1
		else:
			temp1 = temp1
	else:
		temp1 = prey[1] - temp1
	temp1 = min(prey[1], temp4)
	temp3 = prey[1] - temp0
	temp3 = min(prey[1], temp3)
	if temp1 != 0:
		temp1 = temp0 % temp1
	else:
		temp1 = temp1
	temp3 = temp4 * temp4
	if temp3 != 0:
		temp4 = prey[1] / temp3
	else:
		temp4 = temp3
	if temp2 != 0:
		temp1 = temp0 % temp2
	else:
		temp1 = temp2
	temp4 = -1 * temp2
	temp1 = max(temp3, temp0)
	return [prey[1], temp2]
