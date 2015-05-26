#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		temp0 = prey[1] - prey[0]
	else:
		temp0 = prey[0] * prey[1]
	temp1 = prey[0] * prey[0]
	temp2 = max(temp1, temp1)
	if temp2 > temp2:
		temp2 = -1 * prey[0]
	else:
		temp2 = temp1 * prey[0]
	temp2 = min(prey[1], temp1)
	if temp0 != 0:
		temp0 = temp2 % temp0
	else:
		temp0 = temp0
	temp3 = min(prey[0], temp0)
	temp2 = prey[1] * prey[1]
	temp4 = temp0 * temp0
	temp4 = temp4 + temp1
	if temp4 != 0:
		temp4 = temp0 % temp4
	else:
		temp4 = temp4
	temp0 = max(temp1, temp2)
	temp4 = -1 * prey[1]
	temp3 = temp3 - prey[1]
	temp1 = min(temp3, temp3)
	temp0 = prey[1] + temp2
	temp5 = max(temp2, temp4)
	temp1 = -1 * temp4
	temp6 = temp1 - temp3
	temp1 = -1 * temp5
	if temp3 != 0:
		temp4 = temp1 % temp3
	else:
		temp4 = temp3
	return [temp3, prey[0]]
