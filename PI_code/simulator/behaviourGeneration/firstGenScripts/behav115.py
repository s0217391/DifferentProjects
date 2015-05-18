#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	temp1 = -1 * prey[0]
	if prey[1] > temp1:
		temp0 = -1 * prey[0]
	else:
		if prey[1] != 0:
			temp0 = temp1 % prey[1]
		else:
			temp0 = prey[1]
	temp2 = -1 * prey[0]
	if prey[1] > temp2:
		temp3 = -1 * prey[0]
	else:
		temp3 = temp0 - prey[1]
	temp4 = max(prey[0], temp0)
	temp1 = prey[0] + prey[1]
	if prey[0] != 0:
		temp3 = prey[0] % prey[0]
	else:
		temp3 = prey[0]
	return [prey[1], prey[0]]
