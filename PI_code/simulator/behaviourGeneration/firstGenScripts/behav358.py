#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	temp1 = prey[1] * prey[0]
	temp0 = prey[1] + prey[1]
	temp1 = -1 * prey[0]
	if temp0 != 0:
		temp0 = temp0 % temp0
	else:
		temp0 = temp0
	temp0 = temp1 + temp1
	temp2 = temp1 + prey[0]
	return [temp1, prey[1]]
