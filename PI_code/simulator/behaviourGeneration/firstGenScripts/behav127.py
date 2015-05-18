#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = temp0 - prey[1]
	temp1 = min(prey[1], temp1)
	temp1 = max(temp0, prey[0])
	temp1 = min(prey[1], prey[1])
	temp2 = prey[0] + temp0
	temp2 = prey[0] + prey[1]
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	if temp1 != 0:
		temp3 = temp1 % temp1
	else:
		temp3 = temp1
	temp2 = temp1 - temp3
	temp3 = min(temp1, temp3)
	if temp2 != 0:
		temp0 = temp2 % temp2
	else:
		temp0 = temp2
	temp4 = min(temp3, temp1)
	if prey[1] != 0:
		temp5 = temp1 / prey[1]
	else:
		temp5 = prey[1]
	temp6 = -1 * temp3
	temp5 = max(temp1, temp5)
	return [prey[1], temp3]
