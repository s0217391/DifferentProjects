#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	if prey[1] > temp0:
		if prey[0] != 0:
			temp1 = temp0 % prey[0]
		else:
			temp1 = prey[0]
	else:
		if prey[1] != 0:
			temp1 = temp0 % prey[1]
		else:
			temp1 = prey[1]
	if temp0 > temp1:
		if temp0 != 0:
			temp1 = prey[1] / temp0
		else:
			temp1 = temp0
	else:
		temp1 = temp1 + temp1
	temp1 = min(temp0, temp0)
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	if prey[1] != 0:
		temp0 = temp0 / prey[1]
	else:
		temp0 = prey[1]
	temp2 = temp0 * prey[1]
	temp1 = temp1 + temp2
	if prey[1] != 0:
		temp3 = temp1 % prey[1]
	else:
		temp3 = prey[1]
	temp4 = temp2 * temp2
	temp4 = -1 * temp3
	temp2 = temp2 + temp0
	temp3 = prey[0] - prey[1]
	if temp4 != 0:
		temp1 = temp4 % temp4
	else:
		temp1 = temp4
	temp4 = temp3 * temp3
	temp0 = prey[1] * prey[0]
	temp4 = temp0 - prey[0]
	temp0 = temp1 + temp3
	temp5 = temp3 - temp0
	temp0 = temp2 + temp1
	temp3 = min(temp0, temp3)
	if temp3 != 0:
		temp6 = temp3 / temp3
	else:
		temp6 = temp3
	temp4 = prey[0] * temp0
	if temp5 != 0:
		temp3 = prey[0] % temp5
	else:
		temp3 = temp5
	if temp0 != 0:
		temp3 = temp3 / temp0
	else:
		temp3 = temp0
	return [temp5, temp5]
