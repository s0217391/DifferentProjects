#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[1]
	temp1 = temp0 + prey[1]
	temp1 = prey[1] * temp0
	temp0 = temp0 * prey[0]
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	if temp1 > prey[1]:
		if prey[0] > temp0:
			temp0 = temp1 + prey[0]
		else:
			if prey[1] > temp0:
				temp0 = temp1 + temp1
			else:
				temp0 = min(temp1, temp0)
	else:
		if temp1 > temp1:
			if temp0 != 0:
				temp0 = prey[1] / temp0
			else:
				temp0 = temp0
		else:
			if prey[0] != 0:
				temp0 = prey[0] / prey[0]
			else:
				temp0 = prey[0]
	temp0 = max(temp0, temp0)
	return [prey[1], prey[1]]
