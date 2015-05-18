#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[1])
	temp1 = -1 * prey[0]
	temp2 = prey[1] * prey[0]
	if temp2 != 0:
		temp2 = temp1 % temp2
	else:
		temp2 = temp2
	if temp1 > temp2:
		temp2 = -1 * temp1
	else:
		temp2 = max(temp2, temp1)
	temp3 = prey[0] - prey[1]
	temp0 = max(temp2, temp3)
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	temp3 = prey[0] - temp2
	if temp2 != 0:
		temp3 = temp0 % temp2
	else:
		temp3 = temp2
	temp3 = temp2 * temp2
	return [prey[0], temp0]
