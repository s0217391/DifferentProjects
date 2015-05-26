#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = max(prey[1], prey[0])
	temp1 = -1 * temp0
	temp1 = min(temp0, prey[1])
	temp2 = min(temp0, temp0)
	if temp0 != 0:
		temp0 = prey[0] % temp0
	else:
		temp0 = temp0
	temp1 = temp0 + temp2
	temp0 = min(prey[1], temp1)
	temp0 = max(prey[1], prey[1])
	if temp1 != 0:
		temp0 = temp2 % temp1
	else:
		temp0 = temp1
	temp1 = temp1 - temp2
	if temp0 > temp1:
		if temp1 > prey[1]:
			temp3 = temp0 - temp0
		else:
			temp3 = prey[0] * prey[0]
	else:
		temp3 = -1 * temp0
	if temp0 != 0:
		temp0 = temp0 / temp0
	else:
		temp0 = temp0
	temp0 = temp1 * temp0
	return [temp2, prey[0]]
