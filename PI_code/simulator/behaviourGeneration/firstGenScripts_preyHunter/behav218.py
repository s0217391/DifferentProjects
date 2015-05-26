#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[0]
	temp1 = temp0 * prey[1]
	temp0 = temp0 + prey[1]
	if prey[1] > temp1:
		temp2 = temp1 - temp0
	else:
		if prey[1] != 0:
			temp2 = temp0 / prey[1]
		else:
			temp2 = prey[1]
	if temp2 > prey[0]:
		temp1 = prey[1] + temp0
	else:
		if temp2 != 0:
			temp1 = prey[1] % temp2
		else:
			temp1 = temp2
	if temp2 != 0:
		temp0 = prey[1] % temp2
	else:
		temp0 = temp2
	temp0 = prey[1] * temp2
	temp1 = min(prey[1], temp2)
	temp0 = temp1 * temp0
	if temp0 != 0:
		temp2 = temp2 % temp0
	else:
		temp2 = temp0
	temp2 = prey[1] - temp0
	if temp0 > temp0:
		temp2 = min(prey[1], temp1)
	else:
		temp2 = prey[1] * temp2
	temp3 = max(prey[1], temp1)
	temp3 = prey[1] * prey[0]
	if temp2 != 0:
		temp1 = temp3 / temp2
	else:
		temp1 = temp2
	if prey[0] > prey[0]:
		if prey[0] != 0:
			temp0 = temp0 / prey[0]
		else:
			temp0 = prey[0]
	else:
		temp0 = -1 * temp1
	temp4 = temp3 * temp2
	temp0 = temp4 * prey[1]
	temp2 = -1 * temp4
	temp4 = max(temp3, temp2)
	temp1 = prey[1] + temp1
	temp0 = temp0 * temp2
	temp0 = temp2 + temp3
	temp1 = max(temp4, temp2)
	temp0 = max(prey[1], temp4)
	return [temp0, temp3]
