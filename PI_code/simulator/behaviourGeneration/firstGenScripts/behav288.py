#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[0]
	temp1 = temp0 + temp0
	temp2 = prey[1] + prey[1]
	temp0 = temp0 - prey[0]
	temp1 = prey[1] * prey[0]
	temp3 = max(prey[1], temp1)
	temp0 = -1 * temp2
	temp2 = temp2 * temp1
	temp1 = temp3 - temp2
	temp2 = temp1 * temp2
	temp3 = temp2 * temp1
	temp4 = temp1 - temp2
	if prey[1] > temp0:
		temp0 = min(temp1, temp1)
	else:
		if prey[0] != 0:
			temp0 = temp3 % prey[0]
		else:
			temp0 = prey[0]
	temp3 = max(prey[0], temp0)
	if temp2 != 0:
		temp3 = temp1 / temp2
	else:
		temp3 = temp2
	return [temp3, prey[1]]