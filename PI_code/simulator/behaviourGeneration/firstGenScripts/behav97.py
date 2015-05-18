#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	if temp0 > prey[1]:
		temp1 = prey[1] * prey[1]
	else:
		temp1 = prey[0] + temp0
	temp2 = min(temp1, temp0)
	temp0 = temp2 + temp2
	temp2 = temp2 - temp2
	temp2 = temp1 * prey[0]
	if temp1 > temp2:
		temp0 = min(temp0, temp0)
	else:
		temp0 = -1 * prey[1]
	temp2 = temp0 * prey[0]
	temp0 = -1 * temp0
	if temp1 != 0:
		temp2 = temp1 % temp1
	else:
		temp2 = temp1
	temp0 = prey[1] * prey[0]
	return [temp1, temp1]
