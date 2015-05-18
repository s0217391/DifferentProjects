#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[0])
	temp1 = prey[1] * temp0
	if temp0 != 0:
		temp2 = temp1 % temp0
	else:
		temp2 = temp0
	temp0 = temp0 - prey[0]
	temp1 = max(temp2, prey[0])
	temp2 = prey[1] + temp2
	temp3 = max(temp1, temp1)
	temp1 = max(prey[0], temp2)
	temp0 = prey[0] + prey[1]
	temp2 = temp1 + temp3
	temp0 = -1 * temp0
	if prey[0] != 0:
		temp0 = temp3 % prey[0]
	else:
		temp0 = prey[0]
	temp0 = -1 * temp2
	temp3 = min(prey[0], temp2)
	temp3 = prey[0] - prey[1]
	temp3 = temp0 - temp2
	temp1 = temp1 + temp3
	temp2 = max(temp1, temp2)
	temp3 = temp3 * temp0
	if temp3 > prey[0]:
		temp2 = min(temp0, prey[1])
	else:
		if temp2 > temp2:
			if prey[0] != 0:
				temp2 = temp2 / prey[0]
			else:
				temp2 = prey[0]
		else:
			temp2 = temp1 * prey[1]
	temp3 = min(prey[0], prey[1])
	return [temp1, temp3]
