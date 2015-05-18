#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[0]:
		if prey[0] > prey[0]:
			temp0 = prey[0] + prey[0]
		else:
			temp0 = prey[1] + prey[1]
	else:
		if prey[1] != 0:
			temp0 = prey[0] / prey[1]
		else:
			temp0 = prey[1]
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	temp1 = max(temp0, temp0)
	temp2 = temp0 * prey[0]
	if temp0 > prey[0]:
		temp0 = temp0 + temp2
	else:
		if prey[0] != 0:
			temp0 = prey[0] / prey[0]
		else:
			temp0 = prey[0]
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp0 = prey[1] + temp2
	temp0 = prey[0] + temp1
	temp3 = -1 * prey[1]
	temp0 = temp2 + temp1
	temp1 = temp3 * prey[1]
	if temp2 > prey[1]:
		if prey[1] != 0:
			temp0 = temp0 % prey[1]
		else:
			temp0 = prey[1]
	else:
		temp0 = min(temp1, temp3)
	if temp0 != 0:
		temp1 = temp2 % temp0
	else:
		temp1 = temp0
	temp4 = min(temp1, temp2)
	temp5 = min(temp4, prey[1])
	temp2 = -1 * temp1
	temp3 = min(temp3, temp1)
	if temp1 != 0:
		temp5 = temp5 % temp1
	else:
		temp5 = temp1
	temp5 = prey[1] - temp4
	temp2 = max(temp4, temp2)
	temp0 = temp5 - prey[1]
	temp4 = temp2 * temp3
	return [temp0, temp3]
