#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = max(prey[1], temp0)
	if temp1 > prey[1]:
		temp1 = -1 * prey[0]
	else:
		temp1 = prey[1] + prey[0]
	temp0 = min(prey[0], temp1)
	if prey[1] != 0:
		temp0 = temp1 / prey[1]
	else:
		temp0 = prey[1]
	temp0 = prey[0] - prey[0]
	temp1 = temp1 * prey[1]
	temp0 = temp0 - prey[1]
	if prey[0] > temp1:
		temp2 = max(temp0, prey[0])
	else:
		temp2 = temp0 * prey[1]
	temp1 = prey[0] + temp2
	temp3 = max(prey[1], temp2)
	if temp0 > temp2:
		temp4 = max(temp1, temp1)
	else:
		if prey[0] > temp3:
			temp4 = temp0 - prey[1]
		else:
			if temp3 != 0:
				temp4 = prey[1] / temp3
			else:
				temp4 = temp3
	temp5 = -1 * prey[1]
	temp2 = temp5 - temp0
	temp2 = temp4 + temp3
	temp0 = min(prey[1], temp1)
	temp6 = max(temp5, temp1)
	temp4 = min(temp1, temp1)
	temp6 = prey[0] - prey[1]
	if prey[0] != 0:
		temp4 = temp4 / prey[0]
	else:
		temp4 = prey[0]
	temp1 = prey[0] + temp4
	temp5 = max(temp4, temp4)
	return [temp3, temp0]
