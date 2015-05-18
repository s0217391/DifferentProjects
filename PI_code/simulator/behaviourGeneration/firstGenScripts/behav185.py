#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[1]
	temp1 = -1 * prey[1]
	if prey[0] > prey[1]:
		temp2 = min(temp0, temp1)
	else:
		temp2 = prey[1] + prey[0]
	if prey[0] > prey[0]:
		if temp2 != 0:
			temp3 = temp0 % temp2
		else:
			temp3 = temp2
	else:
		temp3 = max(temp1, temp1)
	if temp1 != 0:
		temp3 = prey[1] % temp1
	else:
		temp3 = temp1
	temp3 = prey[1] * temp1
	if temp2 != 0:
		temp3 = temp0 % temp2
	else:
		temp3 = temp2
	if prey[1] != 0:
		temp2 = temp2 / prey[1]
	else:
		temp2 = prey[1]
	temp1 = prey[1] * temp3
	return [prey[0], temp3]
