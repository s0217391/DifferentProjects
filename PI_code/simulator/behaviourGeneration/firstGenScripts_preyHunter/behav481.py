#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		temp0 = -1 * prey[0]
	else:
		if prey[0] > prey[0]:
			temp0 = -1 * prey[0]
		else:
			temp0 = prey[1] - prey[1]
	temp1 = min(temp0, prey[0])
	temp2 = min(prey[1], temp0)
	temp0 = temp0 + prey[1]
	if prey[0] > prey[0]:
		if prey[1] != 0:
			temp2 = temp1 % prey[1]
		else:
			temp2 = prey[1]
	else:
		temp2 = -1 * temp2
	temp2 = min(temp1, temp0)
	temp3 = min(prey[0], temp1)
	if prey[0] != 0:
		temp3 = temp0 % prey[0]
	else:
		temp3 = prey[0]
	if temp3 != 0:
		temp1 = prey[1] % temp3
	else:
		temp1 = temp3
	temp0 = prey[1] - prey[1]
	if temp3 != 0:
		temp4 = temp1 / temp3
	else:
		temp4 = temp3
	temp0 = min(temp2, temp4)
	return [temp3, temp4]