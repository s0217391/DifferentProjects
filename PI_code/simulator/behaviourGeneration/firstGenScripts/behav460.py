#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = min(prey[0], temp0)
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	if prey[1] != 0:
		temp1 = prey[1] % prey[1]
	else:
		temp1 = prey[1]
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	if prey[0] > temp0:
		temp0 = max(temp0, temp0)
	else:
		temp0 = prey[1] + prey[0]
	temp1 = temp1 - temp0
	temp0 = temp0 + temp0
	temp2 = prey[0] + temp0
	temp0 = min(prey[1], prey[1])
	temp2 = prey[1] + prey[0]
	if prey[1] > temp2:
		temp0 = temp1 * temp1
	else:
		if prey[1] > temp1:
			temp0 = temp2 + temp2
		else:
			temp0 = temp2 - temp2
	temp1 = max(temp1, temp0)
	temp2 = min(prey[0], temp0)
	temp1 = temp2 - prey[1]
	temp0 = max(prey[0], prey[0])
	temp3 = prey[0] + temp2
	temp2 = -1 * prey[1]
	if temp0 != 0:
		temp0 = temp1 % temp0
	else:
		temp0 = temp0
	temp2 = temp2 * temp2
	temp4 = -1 * temp1
	if temp3 != 0:
		temp1 = prey[1] / temp3
	else:
		temp1 = temp3
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	temp2 = prey[0] - prey[1]
	if temp1 != 0:
		temp1 = temp1 / temp1
	else:
		temp1 = temp1
	return [temp1, temp1]
