#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[1]
	temp1 = -1 * temp0
	temp2 = prey[0] - temp1
	temp2 = max(prey[0], prey[0])
	temp1 = min(temp2, prey[0])
	temp0 = -1 * temp1
	temp1 = temp1 * prey[1]
	temp1 = max(temp1, prey[1])
	temp1 = prey[0] - prey[1]
	temp1 = temp2 * prey[0]
	temp3 = prey[1] + temp2
	temp4 = -1 * prey[1]
	if prey[0] != 0:
		temp3 = temp0 % prey[0]
	else:
		temp3 = prey[0]
	temp2 = temp1 - prey[1]
	temp1 = -1 * temp3
	return [temp2, temp4]
