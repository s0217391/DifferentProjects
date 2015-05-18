#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[0]
	temp1 = -1 * prey[1]
	temp0 = temp0 - prey[0]
	temp1 = temp1 - temp1
	temp2 = min(temp1, prey[0])
	if temp2 > temp0:
		temp0 = -1 * temp0
	else:
		if temp2 > temp1:
			temp0 = prey[1] + prey[1]
		else:
			temp0 = prey[1] + temp1
	temp0 = prey[0] * temp1
	temp2 = temp0 - temp2
	if prey[1] > prey[1]:
		temp2 = prey[1] * temp2
	else:
		if temp2 != 0:
			temp2 = prey[1] / temp2
		else:
			temp2 = temp2
	if temp0 != 0:
		temp0 = prey[1] / temp0
	else:
		temp0 = temp0
	temp0 = -1 * prey[0]
	temp0 = prey[0] + temp1
	temp1 = -1 * temp2
	temp3 = prey[1] + temp1
	temp3 = temp3 - temp0
	temp1 = max(temp3, prey[1])
	if temp2 != 0:
		temp3 = temp2 / temp2
	else:
		temp3 = temp2
	return [prey[0], prey[0]]
