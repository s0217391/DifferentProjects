#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		temp0 = prey[0] * prey[1]
	else:
		temp0 = -1 * prey[1]
	temp1 = prey[0] * prey[0]
	if temp0 != 0:
		temp1 = temp1 / temp0
	else:
		temp1 = temp0
	if prey[1] > temp1:
		if temp1 != 0:
			temp0 = temp1 / temp1
		else:
			temp0 = temp1
	else:
		temp0 = min(temp1, prey[0])
	temp2 = -1 * temp0
	return [temp2, temp2]
