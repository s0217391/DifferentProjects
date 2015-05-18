#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = -1 * prey[0]
	temp0 = -1 * prey[0]
	temp1 = temp0 + prey[1]
	temp1 = temp0 * prey[1]
	temp1 = temp1 + temp1
	temp0 = min(temp1, prey[0])
	temp1 = min(prey[1], temp1)
	temp1 = temp0 - prey[0]
	if prey[0] != 0:
		temp1 = temp0 % prey[0]
	else:
		temp1 = prey[0]
	temp0 = max(prey[0], temp1)
	temp2 = prey[1] * prey[1]
	temp0 = min(prey[0], temp0)
	if temp1 > temp0:
		if temp0 != 0:
			temp2 = temp2 / temp0
		else:
			temp2 = temp0
	else:
		temp2 = max(prey[1], temp2)
	if temp1 > prey[0]:
		temp3 = max(prey[0], temp2)
	else:
		if prey[0] > prey[0]:
			if temp0 != 0:
				temp3 = prey[1] % temp0
			else:
				temp3 = temp0
		else:
			temp3 = prey[0] - prey[1]
	return [temp1, temp0]
