#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[0]:
		temp0 = -1 * prey[1]
	else:
		if prey[1] > prey[0]:
			temp0 = min(prey[0], prey[0])
		else:
			temp0 = max(prey[0], prey[1])
	temp1 = prey[1] + prey[1]
	if temp1 != 0:
		temp1 = temp1 % temp1
	else:
		temp1 = temp1
	temp2 = max(prey[1], prey[0])
	if prey[1] > prey[0]:
		if temp0 > prey[1]:
			temp3 = temp2 - temp0
		else:
			if temp1 != 0:
				temp3 = temp0 % temp1
			else:
				temp3 = temp1
	else:
		temp3 = -1 * temp2
	temp4 = -1 * temp1
	temp3 = temp4 - temp0
	temp3 = temp3 - temp1
	temp2 = temp4 - prey[0]
	temp1 = temp2 * prey[1]
	if temp2 != 0:
		temp3 = temp0 / temp2
	else:
		temp3 = temp2
	if temp3 != 0:
		temp5 = temp4 % temp3
	else:
		temp5 = temp3
	if temp5 != 0:
		temp2 = temp3 % temp5
	else:
		temp2 = temp5
	temp0 = max(prey[0], temp1)
	return [prey[0], prey[1]]
