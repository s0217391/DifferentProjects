#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[0]
	temp1 = prey[0] * prey[1]
	if temp0 != 0:
		temp0 = temp0 % temp0
	else:
		temp0 = temp0
	temp2 = temp1 - temp0
	temp0 = max(temp0, temp1)
	temp0 = min(temp2, temp2)
	temp1 = min(prey[1], temp2)
	if temp0 != 0:
		temp2 = prey[1] % temp0
	else:
		temp2 = temp0
	temp0 = -1 * prey[0]
	if prey[0] != 0:
		temp2 = prey[1] / prey[0]
	else:
		temp2 = prey[0]
	temp2 = prey[0] + temp1
	if temp2 != 0:
		temp1 = temp1 / temp2
	else:
		temp1 = temp2
	if prey[0] != 0:
		temp2 = temp1 / prey[0]
	else:
		temp2 = prey[0]
	return [temp2, temp1]
