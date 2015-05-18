#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[1]
	temp1 = temp0 * prey[1]
	temp0 = -1 * temp1
	temp0 = temp1 - prey[0]
	temp2 = temp0 * temp1
	temp1 = -1 * temp0
	temp2 = temp0 - prey[0]
	temp3 = prey[0] - temp2
	return [prey[0], prey[0]]
