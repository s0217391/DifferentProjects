#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[1]
	temp1 = max(temp0, temp0)
	if prey[0] > temp0:
		temp1 = temp1 - temp0
	else:
		temp1 = temp0 + temp1
	temp2 = temp0 - prey[0]
	temp3 = prey[0] + temp1
	if prey[0] > temp0:
		if temp0 != 0:
			temp4 = prey[0] / temp0
		else:
			temp4 = temp0
	else:
		temp4 = max(temp0, temp1)
	if prey[0] != 0:
		temp5 = prey[0] / prey[0]
	else:
		temp5 = prey[0]
	if prey[0] > prey[1]:
		temp6 = -1 * temp3
	else:
		if temp4 != 0:
			temp6 = prey[1] / temp4
		else:
			temp6 = temp4
	if temp1 != 0:
		temp3 = temp6 % temp1
	else:
		temp3 = temp1
	temp2 = temp0 - temp0
	temp7 = min(temp4, prey[1])
	return [prey[0], temp4]
