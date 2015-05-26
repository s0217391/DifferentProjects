#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	if temp0 > prey[0]:
		if prey[1] != 0:
			temp1 = prey[0] % prey[1]
		else:
			temp1 = prey[1]
	else:
		temp1 = temp0 - temp0
	temp0 = prey[1] + prey[1]
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	if temp0 > temp0:
		temp0 = prey[1] * temp1
	else:
		temp0 = max(prey[1], prey[0])
	temp2 = -1 * prey[1]
	temp3 = -1 * temp0
	temp4 = min(prey[0], temp3)
	temp5 = temp4 * temp1
	temp4 = prey[0] - prey[0]
	return [temp3, temp3]
