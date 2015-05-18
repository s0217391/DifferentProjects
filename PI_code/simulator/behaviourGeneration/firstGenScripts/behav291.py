#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[1])
	temp1 = prey[1] - temp0
	temp1 = max(prey[0], prey[1])
	if temp1 != 0:
		temp2 = prey[1] / temp1
	else:
		temp2 = temp1
	temp1 = -1 * temp1
	temp3 = prey[1] - temp0
	temp0 = temp2 - prey[0]
	if prey[0] != 0:
		temp3 = temp3 / prey[0]
	else:
		temp3 = prey[0]
	temp1 = prey[0] + temp2
	temp3 = prey[1] + temp2
	if prey[1] != 0:
		temp2 = temp3 % prey[1]
	else:
		temp2 = prey[1]
	temp0 = prey[0] - temp2
	temp4 = max(temp3, temp0)
	temp4 = -1 * temp1
	if temp4 > prey[1]:
		temp4 = prey[1] - temp1
	else:
		temp4 = temp0 * temp1
	return [temp1, prey[0]]
