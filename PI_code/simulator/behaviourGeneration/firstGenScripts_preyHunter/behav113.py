#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = temp0 - prey[1]
	temp2 = max(prey[0], temp1)
	temp0 = max(temp1, prey[0])
	temp2 = temp2 * temp2
	temp3 = prey[0] + temp1
	if temp1 != 0:
		temp4 = temp1 / temp1
	else:
		temp4 = temp1
	if prey[1] != 0:
		temp0 = temp2 / prey[1]
	else:
		temp0 = prey[1]
	temp5 = prey[0] - temp2
	if temp2 != 0:
		temp5 = temp1 / temp2
	else:
		temp5 = temp2
	temp3 = max(prey[0], temp3)
	temp4 = -1 * temp1
	temp2 = max(temp4, temp2)
	if prey[0] != 0:
		temp5 = temp2 % prey[0]
	else:
		temp5 = prey[0]
	return [prey[1], temp0]
