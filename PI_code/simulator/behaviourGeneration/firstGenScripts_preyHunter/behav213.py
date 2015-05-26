#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = prey[1] - prey[0]
	temp2 = temp0 * temp1
	if temp2 != 0:
		temp0 = temp0 / temp2
	else:
		temp0 = temp2
	if prey[0] != 0:
		temp3 = prey[1] % prey[0]
	else:
		temp3 = prey[0]
	temp4 = -1 * temp0
	temp1 = min(prey[1], temp2)
	temp3 = prey[0] * prey[1]
	if prey[1] != 0:
		temp2 = temp0 / prey[1]
	else:
		temp2 = prey[1]
	if temp0 != 0:
		temp5 = temp0 / temp0
	else:
		temp5 = temp0
	return [prey[0], temp3]
