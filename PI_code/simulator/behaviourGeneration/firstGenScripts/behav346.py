#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[0]
	temp1 = temp0 - temp0
	if prey[1] > prey[1]:
		if temp0 > temp0:
			temp0 = max(temp0, temp1)
		else:
			if temp0 != 0:
				temp0 = temp0 % temp0
			else:
				temp0 = temp0
	else:
		temp0 = max(temp1, temp0)
	temp1 = max(prey[1], temp1)
	if prey[0] > prey[1]:
		if prey[0] != 0:
			temp2 = temp0 / prey[0]
		else:
			temp2 = prey[0]
	else:
		if prey[1] != 0:
			temp2 = prey[0] / prey[1]
		else:
			temp2 = prey[1]
	temp2 = temp2 * temp0
	temp3 = -1 * temp2
	if temp0 != 0:
		temp3 = prey[0] / temp0
	else:
		temp3 = temp0
	if temp3 != 0:
		temp0 = prey[1] % temp3
	else:
		temp0 = temp3
	temp4 = -1 * temp3
	temp4 = min(temp0, temp2)
	if temp1 != 0:
		temp1 = temp0 / temp1
	else:
		temp1 = temp1
	temp0 = max(temp2, prey[0])
	temp3 = -1 * temp1
	temp2 = prey[0] - temp4
	temp1 = max(temp2, temp4)
	if prey[0] > prey[0]:
		temp0 = min(temp1, temp2)
	else:
		temp0 = -1 * prey[1]
	if temp3 != 0:
		temp0 = temp3 % temp3
	else:
		temp0 = temp3
	if temp4 > temp1:
		temp0 = max(temp2, temp0)
	else:
		if prey[0] > temp4:
			if temp1 != 0:
				temp0 = temp0 % temp1
			else:
				temp0 = temp1
		else:
			temp0 = temp0 + temp2
	temp0 = prey[1] * temp1
	return [temp2, temp1]
