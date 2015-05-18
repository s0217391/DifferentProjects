#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[0]:
		if prey[1] > prey[0]:
			temp0 = max(prey[1], prey[0])
		else:
			temp0 = min(prey[0], prey[0])
	else:
		temp0 = prey[1] * prey[0]
	temp1 = -1 * prey[0]
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	if prey[1] != 0:
		temp1 = prey[0] % prey[1]
	else:
		temp1 = prey[1]
	if temp0 > prey[1]:
		temp1 = temp0 * temp1
	else:
		temp1 = min(temp0, temp0)
	temp2 = -1 * temp0
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	temp3 = -1 * temp2
	temp0 = temp3 * temp1
	if temp3 > temp0:
		temp3 = min(temp2, temp3)
	else:
		temp3 = max(temp3, temp3)
	temp2 = max(prey[0], temp1)
	if temp1 != 0:
		temp1 = temp0 % temp1
	else:
		temp1 = temp1
	temp1 = temp3 + temp1
	temp1 = min(prey[0], prey[1])
	temp3 = max(prey[1], temp1)
	temp0 = temp2 + temp1
	temp3 = prey[1] * prey[0]
	if temp0 != 0:
		temp0 = prey[0] % temp0
	else:
		temp0 = temp0
	temp4 = prey[1] + temp3
	if temp1 > prey[1]:
		if temp3 != 0:
			temp5 = temp3 / temp3
		else:
			temp5 = temp3
	else:
		if temp0 != 0:
			temp5 = temp0 / temp0
		else:
			temp5 = temp0
	temp6 = max(temp3, temp5)
	temp7 = max(temp5, temp5)
	temp1 = temp5 * prey[0]
	return [temp4, temp1]
