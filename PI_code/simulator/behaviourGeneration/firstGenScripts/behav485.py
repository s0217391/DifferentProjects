#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[0])
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp1 = min(temp0, prey[1])
	temp2 = max(temp1, temp1)
	temp3 = min(temp0, prey[1])
	temp1 = temp2 + temp2
	if temp3 > prey[1]:
		if prey[1] > temp2:
			temp0 = min(temp1, prey[0])
		else:
			temp0 = temp0 * prey[0]
	else:
		temp0 = -1 * prey[0]
	temp2 = min(temp3, temp1)
	temp0 = temp2 * temp3
	if prey[1] != 0:
		temp4 = temp0 / prey[1]
	else:
		temp4 = prey[1]
	temp4 = max(prey[1], prey[1])
	if temp0 != 0:
		temp4 = temp3 / temp0
	else:
		temp4 = temp0
	if temp4 != 0:
		temp1 = prey[1] / temp4
	else:
		temp1 = temp4
	temp0 = temp2 - temp1
	temp1 = max(temp0, temp2)
	temp4 = temp3 + temp1
	return [prey[0], prey[0]]
