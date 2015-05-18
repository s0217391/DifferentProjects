#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = prey[1] * temp0
	temp1 = -1 * prey[0]
	temp1 = temp0 + temp1
	temp1 = prey[0] + prey[0]
	temp2 = -1 * prey[0]
	temp0 = temp2 - prey[1]
	temp2 = temp2 + prey[1]
	temp2 = max(prey[1], temp2)
	temp3 = min(prey[0], prey[0])
	temp4 = max(temp1, prey[1])
	temp4 = max(temp2, temp1)
	temp4 = -1 * prey[0]
	temp1 = max(temp1, temp0)
	return [temp3, temp2]
