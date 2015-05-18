#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[0]
	temp1 = min(temp0, temp0)
	temp0 = temp1 + temp1
	temp0 = prey[0] + temp1
	temp1 = -1 * temp1
	return [prey[1], temp1]
