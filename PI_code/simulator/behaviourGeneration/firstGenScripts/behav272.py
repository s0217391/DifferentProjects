#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[1])
	if temp0 > prey[1]:
		if temp0 != 0:
			temp1 = prey[1] % temp0
		else:
			temp1 = temp0
	else:
		temp1 = temp0 * temp0
	temp1 = -1 * temp1
	temp1 = temp1 + prey[0]
	temp0 = max(temp1, temp1)
	if temp1 > prey[0]:
		temp1 = temp1 * temp1
	else:
		if prey[1] != 0:
			temp1 = prey[1] / prey[1]
		else:
			temp1 = prey[1]
	temp1 = min(temp1, temp1)
	temp1 = min(prey[1], temp1)
	temp2 = max(temp1, prey[1])
	if temp2 != 0:
		temp2 = temp0 / temp2
	else:
		temp2 = temp2
	if temp2 != 0:
		temp2 = temp2 / temp2
	else:
		temp2 = temp2
	temp1 = min(temp0, prey[1])
	temp3 = temp1 - prey[1]
	temp1 = -1 * temp2
	return [temp2, temp3]
