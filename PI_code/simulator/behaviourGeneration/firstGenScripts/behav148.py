#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[0]
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	temp2 = max(prey[1], prey[1])
	temp2 = temp1 - prey[0]
	temp3 = max(prey[1], prey[0])
	if temp2 != 0:
		temp4 = prey[1] % temp2
	else:
		temp4 = temp2
	temp2 = prey[0] - prey[1]
	if temp0 > prey[1]:
		if temp3 > temp4:
			if temp2 > temp0:
				temp3 = max(temp3, temp3)
			else:
				temp3 = max(temp2, temp0)
		else:
			temp3 = temp0 - temp3
	else:
		temp3 = prey[0] * prey[0]
	temp0 = max(prey[0], prey[1])
	temp3 = min(temp1, prey[0])
	temp0 = max(temp3, temp1)
	if temp1 != 0:
		temp4 = prey[1] % temp1
	else:
		temp4 = temp1
	temp2 = temp4 + prey[1]
	temp2 = -1 * prey[1]
	temp0 = min(temp0, temp0)
	temp2 = temp0 * prey[1]
	return [prey[0], prey[1]]
