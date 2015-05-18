#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[1])
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp1 = prey[0] * prey[0]
	temp0 = temp0 - temp1
	temp2 = temp0 * prey[0]
	temp0 = -1 * temp2
	temp3 = prey[1] + temp0
	temp1 = max(temp1, temp1)
	temp0 = -1 * temp0
	temp0 = temp0 * temp0
	if temp3 > temp1:
		if prey[0] > temp2:
			if temp2 > temp3:
				temp1 = temp2 - prey[1]
			else:
				temp1 = max(prey[0], prey[0])
		else:
			temp1 = temp2 + temp3
	else:
		temp1 = temp2 - temp3
	if temp1 > temp1:
		temp2 = max(temp3, temp1)
	else:
		if prey[0] != 0:
			temp2 = temp1 % prey[0]
		else:
			temp2 = prey[0]
	temp1 = min(temp1, prey[1])
	if temp2 > temp1:
		if temp1 != 0:
			temp0 = prey[1] / temp1
		else:
			temp0 = temp1
	else:
		temp0 = max(temp3, prey[0])
	return [temp0, prey[0]]
