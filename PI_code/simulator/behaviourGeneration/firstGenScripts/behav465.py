#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[0])
	temp1 = min(temp0, temp0)
	if temp0 > prey[1]:
		if prey[0] > prey[1]:
			temp2 = prey[0] + temp1
		else:
			temp2 = temp0 * temp1
	else:
		if prey[0] != 0:
			temp2 = temp0 % prey[0]
		else:
			temp2 = prey[0]
	if prey[1] != 0:
		temp0 = temp1 % prey[1]
	else:
		temp0 = prey[1]
	temp2 = max(prey[1], prey[1])
	if prey[0] != 0:
		temp2 = prey[1] % prey[0]
	else:
		temp2 = prey[0]
	temp1 = prey[1] - prey[0]
	temp3 = prey[0] * temp1
	temp3 = prey[1] + temp0
	return [prey[0], temp2]
