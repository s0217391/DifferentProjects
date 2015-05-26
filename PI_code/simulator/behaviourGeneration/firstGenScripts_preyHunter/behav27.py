#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[1]
	if temp0 != 0:
		temp1 = prey[1] % temp0
	else:
		temp1 = temp0
	temp2 = -1 * temp1
	temp3 = -1 * temp2
	temp1 = temp0 - temp3
	temp4 = prey[0] + prey[1]
	temp0 = temp3 + temp1
	if temp4 > temp4:
		temp2 = min(temp1, prey[0])
	else:
		temp2 = max(prey[0], temp0)
	temp4 = -1 * temp1
	if temp2 > prey[0]:
		temp0 = temp4 + prey[0]
	else:
		temp0 = min(temp3, temp4)
	temp4 = min(temp0, prey[0])
	temp3 = max(temp2, temp1)
	if prey[0] > temp0:
		temp3 = min(prey[1], temp2)
	else:
		temp3 = prey[0] + temp2
	temp5 = max(temp2, temp0)
	temp0 = -1 * temp0
	if temp1 != 0:
		temp1 = temp3 / temp1
	else:
		temp1 = temp1
	if temp5 != 0:
		temp3 = prey[1] / temp5
	else:
		temp3 = temp5
	temp1 = temp1 + temp1
	temp0 = -1 * prey[0]
	if temp3 != 0:
		temp1 = temp2 % temp3
	else:
		temp1 = temp3
	return [temp2, temp5]
