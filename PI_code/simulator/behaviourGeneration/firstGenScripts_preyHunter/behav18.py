#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[1]:
		if prey[0] != 0:
			temp0 = prey[1] / prey[0]
		else:
			temp0 = prey[0]
	else:
		temp0 = prey[1] * prey[0]
	temp1 = min(prey[0], temp0)
	if temp1 != 0:
		temp0 = temp0 % temp1
	else:
		temp0 = temp1
	if prey[0] != 0:
		temp2 = prey[1] / prey[0]
	else:
		temp2 = prey[0]
	temp3 = prey[0] - temp2
	temp1 = temp0 + temp0
	if temp1 > temp1:
		temp3 = min(temp2, temp1)
	else:
		temp3 = max(prey[0], temp3)
	temp1 = prey[0] * temp1
	temp3 = min(prey[1], temp2)
	temp1 = temp1 + temp3
	temp3 = min(temp3, temp0)
	temp0 = temp3 * prey[0]
	if temp2 > temp3:
		temp2 = temp0 + temp3
	else:
		temp2 = temp1 + temp1
	temp1 = temp0 - temp2
	temp2 = max(temp0, temp2)
	return [prey[1], temp0]
