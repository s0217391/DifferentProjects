#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = temp0 * prey[0]
	temp1 = prey[1] + prey[0]
	temp2 = max(temp1, prey[0])
	temp3 = temp1 + temp1
	if prey[1] > prey[0]:
		temp4 = temp0 + prey[1]
	else:
		temp4 = temp1 + prey[0]
	temp1 = temp4 * temp2
	temp5 = temp1 * temp0
	temp6 = min(temp4, prey[0])
	if temp5 > temp4:
		temp6 = -1 * temp6
	else:
		if temp2 > temp4:
			temp6 = prey[0] + temp4
		else:
			temp6 = max(temp6, temp5)
	if temp2 > prey[0]:
		temp2 = temp6 * prey[1]
	else:
		temp2 = temp1 * temp4
	temp3 = temp0 * prey[0]
	temp3 = min(temp0, temp6)
	temp0 = -1 * temp1
	temp4 = temp0 * temp0
	temp3 = max(temp6, temp2)
	return [prey[1], temp4]
