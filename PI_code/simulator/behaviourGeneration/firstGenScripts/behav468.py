#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[0])
	temp1 = prey[0] * temp0
	temp0 = min(prey[1], prey[1])
	if temp0 != 0:
		temp2 = prey[1] / temp0
	else:
		temp2 = temp0
	temp2 = prey[1] * temp0
	if prey[1] != 0:
		temp2 = temp2 % prey[1]
	else:
		temp2 = prey[1]
	if temp2 != 0:
		temp1 = temp2 % temp2
	else:
		temp1 = temp2
	temp0 = min(temp0, prey[1])
	return [prey[1], prey[1]]
