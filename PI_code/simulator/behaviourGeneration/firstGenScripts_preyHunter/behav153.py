#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[1])
	temp1 = -1 * prey[0]
	if prey[0] != 0:
		temp2 = temp0 / prey[0]
	else:
		temp2 = prey[0]
	temp1 = max(prey[1], prey[1])
	temp1 = -1 * temp1
	if prey[0] > prey[0]:
		temp1 = temp2 - prey[1]
	else:
		temp1 = temp0 - prey[0]
	if temp1 != 0:
		temp2 = temp2 % temp1
	else:
		temp2 = temp1
	temp0 = -1 * temp1
	temp0 = temp0 * temp2
	temp3 = -1 * prey[1]
	if temp3 != 0:
		temp0 = prey[1] / temp3
	else:
		temp0 = temp3
	if temp1 > temp0:
		temp4 = prey[1] - prey[0]
	else:
		temp4 = min(temp0, prey[0])
	temp2 = max(temp4, temp4)
	temp2 = temp4 + prey[1]
	temp5 = temp1 + temp3
	if temp4 > temp1:
		temp1 = temp1 - temp4
	else:
		if prey[1] != 0:
			temp1 = temp5 / prey[1]
		else:
			temp1 = prey[1]
	temp1 = -1 * temp4
	if prey[1] != 0:
		temp4 = temp2 / prey[1]
	else:
		temp4 = prey[1]
	temp0 = min(temp0, temp4)
	if temp1 > temp2:
		if prey[0] != 0:
			temp4 = temp2 / prey[0]
		else:
			temp4 = prey[0]
	else:
		if temp0 != 0:
			temp4 = temp1 % temp0
		else:
			temp4 = temp0
	if prey[1] != 0:
		temp2 = prey[0] % prey[1]
	else:
		temp2 = prey[1]
	temp4 = temp2 - temp3
	temp4 = temp1 - prey[1]
	if temp3 != 0:
		temp3 = temp5 % temp3
	else:
		temp3 = temp3
	temp2 = -1 * temp1
	return [temp1, temp0]
