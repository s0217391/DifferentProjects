#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[1])
	if prey[0] > temp0:
		temp1 = prey[0] * prey[0]
	else:
		if prey[1] > prey[1]:
			temp1 = -1 * prey[1]
		else:
			temp1 = min(prey[0], prey[0])
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	temp2 = prey[1] - temp0
	temp2 = max(temp0, temp0)
	temp0 = prey[0] - temp2
	temp0 = max(temp0, temp2)
	temp3 = min(temp0, prey[1])
	temp1 = min(temp3, temp2)
	temp3 = min(temp3, prey[0])
	temp3 = -1 * temp2
	if prey[0] != 0:
		temp4 = temp0 % prey[0]
	else:
		temp4 = prey[0]
	if prey[1] != 0:
		temp1 = prey[1] % prey[1]
	else:
		temp1 = prey[1]
	temp0 = -1 * temp0
	temp2 = max(prey[0], temp1)
	if temp3 != 0:
		temp0 = prey[0] / temp3
	else:
		temp0 = temp3
	temp1 = prey[0] * temp4
	temp1 = prey[0] * temp1
	temp4 = min(temp2, prey[0])
	temp3 = max(temp2, temp4)
	return [temp0, prey[1]]