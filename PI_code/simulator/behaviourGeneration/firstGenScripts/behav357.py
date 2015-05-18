#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[1])
	temp1 = prey[1] - prey[1]
	temp1 = min(prey[1], temp0)
	if temp0 > prey[0]:
		temp0 = prey[1] - temp1
	else:
		if prey[1] != 0:
			temp0 = temp0 % prey[1]
		else:
			temp0 = prey[1]
	temp1 = -1 * temp1
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = prey[1] - prey[1]
	if prey[0] != 0:
		temp2 = prey[1] / prey[0]
	else:
		temp2 = prey[0]
	temp2 = prey[0] * temp1
	temp0 = prey[0] + prey[0]
	temp3 = min(temp1, prey[0])
	temp4 = max(prey[1], prey[0])
	if prey[1] != 0:
		temp3 = temp0 % prey[1]
	else:
		temp3 = prey[1]
	temp4 = temp3 * temp3
	if temp3 > temp2:
		temp3 = temp0 * prey[1]
	else:
		temp3 = max(temp4, prey[0])
	if temp0 > temp2:
		if prey[0] > temp3:
			if prey[0] != 0:
				temp5 = temp1 % prey[0]
			else:
				temp5 = prey[0]
		else:
			temp5 = prey[0] * temp3
	else:
		temp5 = -1 * temp0
	temp5 = min(prey[0], temp0)
	return [temp4, temp2]
