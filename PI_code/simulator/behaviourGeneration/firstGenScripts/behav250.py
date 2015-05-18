#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		temp0 = max(prey[0], prey[1])
	else:
		if prey[0] > prey[0]:
			if prey[0] > prey[0]:
				temp0 = prey[1] - prey[1]
			else:
				if prey[1] != 0:
					temp0 = prey[0] / prey[1]
				else:
					temp0 = prey[1]
		else:
			temp0 = max(prey[0], prey[1])
	temp1 = prey[0] + prey[1]
	temp2 = prey[0] * temp1
	temp0 = prey[1] - temp2
	temp1 = max(temp2, prey[1])
	temp1 = temp1 * temp0
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp0 = temp1 - temp1
	temp2 = prey[0] - temp1
	return [temp0, temp0]
