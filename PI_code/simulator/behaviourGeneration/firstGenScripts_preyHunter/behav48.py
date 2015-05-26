#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[0])
	temp1 = prey[0] + prey[0]
	temp2 = max(temp1, temp0)
	temp0 = max(temp2, prey[1])
	if temp1 != 0:
		temp2 = temp2 / temp1
	else:
		temp2 = temp1
	temp3 = temp0 + prey[1]
	if temp3 != 0:
		temp1 = prey[1] / temp3
	else:
		temp1 = temp3
	if temp2 != 0:
		temp3 = temp2 % temp2
	else:
		temp3 = temp2
	temp1 = max(temp1, prey[1])
	temp3 = temp1 * temp2
	temp1 = max(temp3, temp0)
	return [temp1, prey[0]]
