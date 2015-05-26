#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	temp1 = temp0 + prey[0]
	if temp0 > temp0:
		if temp0 > prey[0]:
			if prey[1] != 0:
				temp1 = temp1 % prey[1]
			else:
				temp1 = prey[1]
		else:
			temp1 = max(temp1, temp1)
	else:
		temp1 = min(prey[1], temp1)
	temp0 = temp0 - temp1
	temp0 = max(prey[1], temp0)
	if temp1 != 0:
		temp2 = temp0 % temp1
	else:
		temp2 = temp1
	if temp2 > temp1:
		temp0 = prey[0] - temp0
	else:
		if prey[0] > temp0:
			temp0 = prey[0] - temp1
		else:
			if temp1 != 0:
				temp0 = temp2 / temp1
			else:
				temp0 = temp1
	temp3 = max(prey[1], temp0)
	return [prey[1], temp1]
