#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = max(prey[0], prey[0])
	temp2 = -1 * temp1
	if temp2 > temp2:
		if prey[0] != 0:
			temp0 = temp2 % prey[0]
		else:
			temp0 = prey[0]
	else:
		if prey[1] != 0:
			temp0 = temp0 / prey[1]
		else:
			temp0 = prey[1]
	temp2 = max(prey[0], temp1)
	temp3 = temp0 - prey[1]
	temp1 = temp2 + temp3
	temp1 = temp1 - prey[0]
	temp0 = max(temp0, temp3)
	if prey[0] != 0:
		temp4 = prey[1] / prey[0]
	else:
		temp4 = prey[0]
	if temp0 > temp4:
		if prey[0] != 0:
			temp4 = prey[0] / prey[0]
		else:
			temp4 = prey[0]
	else:
		temp4 = min(temp2, temp0)
	temp1 = -1 * temp2
	temp5 = temp1 * prey[1]
	if temp4 != 0:
		temp6 = temp1 / temp4
	else:
		temp6 = temp4
	temp5 = -1 * temp1
	temp1 = -1 * prey[0]
	if temp2 > temp0:
		if prey[1] > temp3:
			temp2 = temp5 * temp5
		else:
			temp2 = temp1 - prey[0]
	else:
		temp2 = max(temp4, temp0)
	if temp0 > temp1:
		temp0 = min(prey[1], prey[1])
	else:
		if temp1 != 0:
			temp0 = temp6 / temp1
		else:
			temp0 = temp1
	temp1 = temp2 - temp2
	temp1 = prey[1] - temp6
	temp1 = prey[1] - temp5
	return [temp1, temp2]