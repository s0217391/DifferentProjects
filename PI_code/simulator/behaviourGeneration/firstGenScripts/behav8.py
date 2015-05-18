#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[0]
	temp1 = prey[0] + prey[0]
	temp0 = min(prey[0], temp0)
	if temp1 != 0:
		temp2 = temp1 / temp1
	else:
		temp2 = temp1
	temp1 = prey[0] - prey[1]
	if temp0 != 0:
		temp2 = prey[0] / temp0
	else:
		temp2 = temp0
	if prey[1] != 0:
		temp0 = temp0 % prey[1]
	else:
		temp0 = prey[1]
	if prey[1] > temp0:
		if prey[1] > prey[0]:
			temp1 = min(prey[0], prey[0])
		else:
			if temp0 != 0:
				temp1 = prey[1] % temp0
			else:
				temp1 = temp0
	else:
		if temp0 != 0:
			temp1 = temp2 % temp0
		else:
			temp1 = temp0
	temp3 = max(prey[0], temp1)
	if temp0 > prey[0]:
		temp4 = max(prey[0], temp2)
	else:
		temp4 = prey[0] - temp0
	return [temp1, temp3]
