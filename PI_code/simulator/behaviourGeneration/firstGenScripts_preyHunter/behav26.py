#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	if prey[0] > prey[0]:
		temp1 = temp0 * prey[1]
	else:
		if temp0 > temp0:
			temp1 = temp0 - prey[1]
		else:
			if prey[1] != 0:
				temp1 = prey[0] / prey[1]
			else:
				temp1 = prey[1]
	temp0 = max(temp0, prey[0])
	temp2 = prey[1] + temp1
	temp2 = min(temp0, prey[0])
	temp3 = temp1 * temp0
	temp2 = max(temp1, prey[0])
	temp0 = prey[1] + temp3
	temp0 = -1 * prey[1]
	if temp0 != 0:
		temp2 = temp0 / temp0
	else:
		temp2 = temp0
	if temp0 != 0:
		temp2 = prey[0] % temp0
	else:
		temp2 = temp0
	return [temp0, temp2]