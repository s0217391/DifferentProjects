#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[0]:
		if prey[1] != 0:
			temp0 = prey[0] / prey[1]
		else:
			temp0 = prey[1]
	else:
		temp0 = min(prey[1], prey[1])
	temp1 = prey[0] + temp0
	if temp1 > temp0:
		if temp0 > prey[1]:
			temp1 = temp1 * prey[1]
		else:
			temp1 = prey[1] + prey[0]
	else:
		temp1 = temp0 - temp0
	if temp0 != 0:
		temp2 = temp0 % temp0
	else:
		temp2 = temp0
	if temp1 > temp0:
		temp0 = max(prey[0], prey[1])
	else:
		temp0 = min(temp0, temp0)
	temp2 = -1 * temp1
	if temp0 != 0:
		temp3 = prey[0] / temp0
	else:
		temp3 = temp0
	temp4 = -1 * temp3
	if temp4 != 0:
		temp5 = temp3 / temp4
	else:
		temp5 = temp4
	temp0 = temp3 * temp3
	if prey[0] != 0:
		temp2 = temp3 % prey[0]
	else:
		temp2 = prey[0]
	temp1 = temp2 * temp4
	temp6 = max(temp2, temp5)
	temp3 = max(prey[0], prey[1])
	if temp6 != 0:
		temp2 = temp1 % temp6
	else:
		temp2 = temp6
	temp4 = prey[1] * temp3
	if temp6 != 0:
		temp2 = temp2 / temp6
	else:
		temp2 = temp6
	temp0 = -1 * temp2
	temp2 = min(temp6, temp4)
	temp4 = temp1 - temp5
	return [temp6, temp0]
