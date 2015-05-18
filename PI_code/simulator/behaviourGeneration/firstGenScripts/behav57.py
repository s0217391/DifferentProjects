#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = min(prey[1], prey[1])
	temp2 = temp0 - prey[0]
	temp1 = temp1 + temp2
	temp2 = min(prey[0], prey[0])
	if prey[0] != 0:
		temp0 = temp1 % prey[0]
	else:
		temp0 = prey[0]
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	temp1 = max(temp2, temp1)
	temp1 = temp2 + temp0
	if prey[0] > prey[0]:
		if prey[1] != 0:
			temp0 = prey[1] / prey[1]
		else:
			temp0 = prey[1]
	else:
		temp0 = prey[1] + temp1
	if prey[0] != 0:
		temp2 = temp1 % prey[0]
	else:
		temp2 = prey[0]
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	temp0 = temp0 - temp1
	if prey[0] != 0:
		temp3 = temp2 / prey[0]
	else:
		temp3 = prey[0]
	temp4 = prey[0] * temp2
	if temp0 != 0:
		temp5 = temp3 / temp0
	else:
		temp5 = temp0
	temp1 = temp3 * prey[0]
	temp6 = temp0 - temp5
	temp4 = temp1 - temp3
	temp3 = temp1 * temp2
	if prey[0] != 0:
		temp0 = temp1 % prey[0]
	else:
		temp0 = prey[0]
	temp6 = min(temp2, prey[0])
	temp7 = temp6 + temp0
	temp3 = prey[1] - temp1
	return [temp6, temp2]
