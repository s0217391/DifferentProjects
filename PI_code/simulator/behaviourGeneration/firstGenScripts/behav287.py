#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[1]
	temp1 = max(temp0, prey[0])
	temp2 = -1 * prey[0]
	if temp2 != 0:
		temp0 = prey[0] / temp2
	else:
		temp0 = temp2
	temp2 = temp0 + temp1
	if temp0 != 0:
		temp3 = prey[1] / temp0
	else:
		temp3 = temp0
	temp2 = -1 * temp2
	temp3 = min(prey[1], temp2)
	if prey[0] > temp1:
		temp0 = prey[1] - prey[1]
	else:
		temp0 = prey[0] * prey[0]
	temp4 = -1 * prey[0]
	if prey[1] > temp3:
		if temp0 > temp2:
			if prey[1] != 0:
				temp1 = temp4 % prey[1]
			else:
				temp1 = prey[1]
		else:
			temp1 = -1 * temp4
	else:
		temp1 = temp1 - temp1
	temp1 = temp0 - prey[1]
	if temp2 != 0:
		temp3 = temp2 % temp2
	else:
		temp3 = temp2
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	return [temp2, prey[1]]
