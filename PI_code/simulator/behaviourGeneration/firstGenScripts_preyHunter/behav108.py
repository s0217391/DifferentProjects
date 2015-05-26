#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = prey[1] - temp0
	temp2 = -1 * prey[1]
	if temp1 != 0:
		temp0 = prey[1] / temp1
	else:
		temp0 = temp1
	temp0 = prey[1] - prey[0]
	if temp1 > prey[1]:
		temp1 = temp2 * temp2
	else:
		if prey[1] != 0:
			temp1 = temp1 % prey[1]
		else:
			temp1 = prey[1]
	temp3 = -1 * temp2
	if temp0 != 0:
		temp3 = temp3 % temp0
	else:
		temp3 = temp0
	return [temp0, temp1]
