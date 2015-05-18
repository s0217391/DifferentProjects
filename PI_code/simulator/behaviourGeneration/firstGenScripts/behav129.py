#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[0]
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	temp0 = temp0 - prey[1]
	temp1 = prey[1] - temp1
	temp0 = min(temp1, temp0)
	if temp0 != 0:
		temp0 = temp1 / temp0
	else:
		temp0 = temp0
	if prey[1] != 0:
		temp1 = prey[1] % prey[1]
	else:
		temp1 = prey[1]
	temp0 = temp1 + prey[1]
	temp2 = -1 * temp1
	if temp1 != 0:
		temp1 = prey[1] % temp1
	else:
		temp1 = temp1
	temp2 = -1 * prey[0]
	if prey[0] != 0:
		temp3 = prey[0] / prey[0]
	else:
		temp3 = prey[0]
	temp2 = -1 * prey[1]
	temp1 = prey[1] + temp3
	if temp1 != 0:
		temp0 = temp1 / temp1
	else:
		temp0 = temp1
	if prey[0] != 0:
		temp4 = prey[0] % prey[0]
	else:
		temp4 = prey[0]
	if temp3 != 0:
		temp3 = temp3 / temp3
	else:
		temp3 = temp3
	if temp4 != 0:
		temp0 = temp1 % temp4
	else:
		temp0 = temp4
	if temp4 != 0:
		temp4 = prey[1] % temp4
	else:
		temp4 = temp4
	if temp4 != 0:
		temp3 = temp3 / temp4
	else:
		temp3 = temp4
	if prey[1] != 0:
		temp1 = temp0 % prey[1]
	else:
		temp1 = prey[1]
	temp1 = prey[1] - temp1
	temp0 = temp1 * temp2
	temp3 = temp0 * temp0
	return [prey[1], temp2]
