#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	temp1 = min(prey[1], prey[0])
	if temp0 != 0:
		temp0 = temp0 % temp0
	else:
		temp0 = temp0
	temp2 = temp0 + prey[1]
	temp0 = prey[1] * temp2
	temp1 = temp2 * temp0
	temp1 = max(temp0, prey[1])
	if temp1 != 0:
		temp2 = temp1 % temp1
	else:
		temp2 = temp1
	if temp0 != 0:
		temp1 = temp1 % temp0
	else:
		temp1 = temp0
	temp2 = -1 * temp1
	if prey[0] != 0:
		temp1 = prey[0] % prey[0]
	else:
		temp1 = prey[0]
	return [temp1, prey[0]]