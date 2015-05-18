#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[1]
	temp1 = -1 * prey[0]
	temp0 = max(temp1, prey[1])
	temp1 = temp0 * temp0
	return [prey[1], temp1]
