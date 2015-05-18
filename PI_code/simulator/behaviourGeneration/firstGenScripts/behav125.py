#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[1])
	temp1 = prey[0] + temp0
	temp1 = min(prey[0], prey[0])
	if prey[1] > prey[0]:
		temp0 = -1 * temp0
	else:
		temp0 = -1 * temp0
	if prey[1] != 0:
		temp1 = temp0 % prey[1]
	else:
		temp1 = prey[1]
	temp2 = -1 * temp0
	temp3 = max(temp1, temp1)
	temp4 = prey[1] - prey[0]
	if temp1 != 0:
		temp3 = temp2 % temp1
	else:
		temp3 = temp1
	if temp0 != 0:
		temp3 = prey[0] % temp0
	else:
		temp3 = temp0
	temp1 = -1 * prey[1]
	if temp0 != 0:
		temp2 = prey[0] % temp0
	else:
		temp2 = temp0
	temp5 = min(prey[1], temp4)
	temp1 = -1 * prey[0]
	temp0 = prey[1] - temp2
	if temp1 > prey[0]:
		temp1 = temp2 + temp0
	else:
		temp1 = min(temp0, temp4)
	temp6 = -1 * temp3
	temp5 = -1 * temp0
	temp3 = -1 * temp2
	temp2 = temp5 * temp2
	temp7 = temp5 * prey[1]
	temp5 = max(temp7, temp1)
	temp6 = temp7 + temp0
	temp2 = temp6 * prey[1]
	if temp2 != 0:
		temp1 = temp2 % temp2
	else:
		temp1 = temp2
	return [temp3, temp5]
