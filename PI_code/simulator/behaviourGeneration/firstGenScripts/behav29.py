#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[0]
	temp1 = min(prey[1], prey[0])
	temp0 = prey[1] + prey[0]
	temp2 = temp0 - temp0
	temp1 = temp1 * prey[0]
	return [prey[1], temp2]
