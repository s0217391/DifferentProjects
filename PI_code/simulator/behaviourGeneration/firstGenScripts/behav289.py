#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[1]
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	temp1 = max(temp1, prey[0])
	temp2 = min(temp1, prey[0])
	temp1 = -1 * prey[0]
	temp2 = max(prey[1], temp1)
	temp2 = max(temp2, temp1)
	temp2 = max(temp2, prey[0])
	if temp2 != 0:
		temp1 = prey[1] / temp2
	else:
		temp1 = temp2
	if temp2 != 0:
		temp0 = prey[0] / temp2
	else:
		temp0 = temp2
	temp2 = prey[0] + prey[1]
	temp1 = max(temp2, prey[0])
	temp1 = temp0 - temp1
	if prey[0] != 0:
		temp0 = temp1 % prey[0]
	else:
		temp0 = prey[0]
	temp2 = max(prey[0], prey[0])
	if temp0 > prey[0]:
		if prey[0] != 0:
			temp1 = prey[1] / prey[0]
		else:
			temp1 = prey[0]
	else:
		if temp2 != 0:
			temp1 = temp2 % temp2
		else:
			temp1 = temp2
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	temp1 = prey[1] - temp0
	temp3 = temp0 - prey[1]
	temp4 = temp1 - temp3
	temp5 = min(temp2, prey[0])
	temp3 = temp5 + temp5
	temp6 = -1 * temp5
	if temp5 > temp2:
		temp2 = prey[0] + prey[0]
	else:
		temp2 = temp1 + temp5
	return [temp5, temp5]
