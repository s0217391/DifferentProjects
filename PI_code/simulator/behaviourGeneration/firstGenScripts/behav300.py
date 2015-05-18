#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = temp1 * temp1
	if prey[0] != 0:
		temp1 = prey[0] % prey[0]
	else:
		temp1 = prey[0]
	temp2 = prey[1] - prey[0]
	temp3 = min(prey[1], prey[0])
	temp4 = temp0 - temp2
	if temp4 > prey[0]:
		temp5 = min(temp2, prey[0])
	else:
		if prey[1] > temp2:
			temp5 = temp0 * prey[1]
		else:
			if temp3 != 0:
				temp5 = temp2 % temp3
			else:
				temp5 = temp3
	temp1 = max(temp0, temp5)
	if temp4 != 0:
		temp2 = temp0 / temp4
	else:
		temp2 = temp4
	return [temp2, temp5]
