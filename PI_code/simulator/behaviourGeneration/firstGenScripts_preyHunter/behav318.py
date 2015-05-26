#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = min(prey[0], prey[1])
	temp2 = -1 * prey[0]
	if prey[1] != 0:
		temp2 = prey[0] % prey[1]
	else:
		temp2 = prey[1]
	if temp1 != 0:
		temp3 = prey[0] % temp1
	else:
		temp3 = temp1
	temp0 = prey[1] - temp1
	temp0 = min(temp2, temp3)
	temp1 = -1 * temp3
	if temp3 > temp0:
		temp2 = temp3 + prey[0]
	else:
		temp2 = min(temp2, prey[1])
	temp4 = min(prey[0], prey[0])
	if prey[1] != 0:
		temp3 = temp4 / prey[1]
	else:
		temp3 = prey[1]
	temp1 = min(prey[0], prey[0])
	temp2 = temp0 - temp4
	return [prey[0], temp0]
