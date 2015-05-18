#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[1])
	temp1 = min(temp0, prey[0])
	temp2 = min(temp1, prey[1])
	temp0 = -1 * prey[1]
	if temp2 > temp0:
		if temp0 > prey[0]:
			temp0 = -1 * prey[0]
		else:
			temp0 = min(prey[0], prey[0])
	else:
		temp0 = prey[0] - temp0
	if prey[0] != 0:
		temp1 = temp1 / prey[0]
	else:
		temp1 = prey[0]
	temp2 = prey[0] - temp2
	temp3 = temp0 * temp0
	temp0 = prey[0] - temp2
	if prey[0] != 0:
		temp3 = temp1 / prey[0]
	else:
		temp3 = prey[0]
	temp0 = min(temp0, temp0)
	if temp2 > temp3:
		temp1 = prey[0] + prey[1]
	else:
		if temp2 != 0:
			temp1 = temp1 % temp2
		else:
			temp1 = temp2
	if temp0 != 0:
		temp1 = prey[0] / temp0
	else:
		temp1 = temp0
	if prey[0] != 0:
		temp3 = temp1 / prey[0]
	else:
		temp3 = prey[0]
	temp3 = -1 * prey[0]
	temp3 = -1 * temp3
	if temp2 != 0:
		temp3 = temp1 / temp2
	else:
		temp3 = temp2
	temp3 = temp1 + temp0
	temp4 = -1 * prey[0]
	if temp3 != 0:
		temp3 = temp3 % temp3
	else:
		temp3 = temp3
	temp2 = temp3 - prey[1]
	temp0 = max(temp0, temp2)
	temp4 = max(temp3, prey[0])
	if temp2 != 0:
		temp4 = prey[0] / temp2
	else:
		temp4 = temp2
	return [temp4, temp0]
