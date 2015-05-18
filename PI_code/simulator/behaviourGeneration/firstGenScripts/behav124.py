#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	temp1 = max(temp0, prey[1])
	temp1 = temp0 * prey[1]
	temp0 = prey[0] * temp1
	return [prey[0], temp0]
