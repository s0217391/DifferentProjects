#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[1]
	if prey[1] > prey[0]:
		if temp0 != 0:
			temp1 = temp0 % temp0
		else:
			temp1 = temp0
	else:
		temp1 = temp0 + prey[0]
	temp0 = min(temp1, temp1)
	temp2 = prey[0] * temp0
	temp2 = prey[0] - prey[1]
	temp2 = min(temp1, temp1)
	temp3 = prey[1] - temp1
	if prey[1] != 0:
		temp0 = temp3 % prey[1]
	else:
		temp0 = prey[1]
	temp3 = temp1 * temp2
	temp3 = prey[0] * temp2
	return [prey[1], temp0]
