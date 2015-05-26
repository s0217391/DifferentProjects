#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[0])
	temp1 = prey[0] - prey[0]
	temp0 = temp1 * prey[1]
	temp0 = max(prey[0], prey[1])
	temp2 = prey[0] + prey[0]
	temp1 = max(prey[1], prey[1])
	if prey[1] != 0:
		temp3 = temp0 % prey[1]
	else:
		temp3 = prey[1]
	temp1 = max(prey[1], temp1)
	if temp2 > temp3:
		temp3 = min(temp0, prey[1])
	else:
		temp3 = max(temp1, prey[0])
	temp3 = temp3 - temp0
	if prey[1] != 0:
		temp3 = prey[0] % prey[1]
	else:
		temp3 = prey[1]
	temp4 = max(temp2, prey[1])
	temp3 = min(prey[0], temp3)
	if prey[1] != 0:
		temp3 = prey[0] / prey[1]
	else:
		temp3 = prey[1]
	temp4 = prey[0] - temp1
	temp2 = temp1 * temp3
	temp2 = prey[0] + prey[0]
	if prey[1] != 0:
		temp4 = prey[1] / prey[1]
	else:
		temp4 = prey[1]
	return [prey[0], prey[1]]
