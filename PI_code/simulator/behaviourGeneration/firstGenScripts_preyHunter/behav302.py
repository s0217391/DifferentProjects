#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[1]:
		temp0 = prey[0] * prey[0]
	else:
		temp0 = max(prey[1], prey[0])
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	temp2 = temp1 - prey[1]
	temp0 = -1 * prey[1]
	temp3 = temp2 - temp0
	temp1 = prey[1] + prey[0]
	temp4 = min(prey[0], prey[0])
	if temp2 != 0:
		temp5 = temp4 % temp2
	else:
		temp5 = temp2
	temp2 = temp1 - temp4
	temp1 = max(temp2, temp0)
	temp5 = -1 * temp0
	if temp1 != 0:
		temp6 = temp0 / temp1
	else:
		temp6 = temp1
	return [temp1, prey[1]]
