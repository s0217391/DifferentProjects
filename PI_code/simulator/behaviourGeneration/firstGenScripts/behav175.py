#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[0])
	temp1 = -1 * prey[1]
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp1 = prey[0] + prey[0]
	temp1 = temp0 * temp0
	temp2 = prey[0] + prey[0]
	temp1 = temp2 + temp0
	if prey[1] != 0:
		temp0 = temp2 / prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * temp2
	if temp2 > prey[0]:
		temp3 = -1 * temp1
	else:
		temp3 = -1 * temp1
	if temp0 > prey[1]:
		temp2 = max(temp3, temp2)
	else:
		temp2 = prey[1] - temp1
	if temp1 != 0:
		temp0 = temp0 % temp1
	else:
		temp0 = temp1
	temp0 = prey[0] - temp3
	temp2 = temp3 - prey[0]
	if prey[0] > temp3:
		temp1 = temp1 + temp3
	else:
		temp1 = -1 * prey[0]
	temp1 = prey[0] - temp3
	if prey[0] > temp1:
		temp1 = max(prey[1], prey[0])
	else:
		temp1 = min(temp3, prey[1])
	temp0 = prey[1] * temp3
	temp3 = max(temp0, prey[1])
	if temp2 != 0:
		temp4 = temp3 / temp2
	else:
		temp4 = temp2
	temp0 = temp0 - prey[0]
	return [temp3, temp4]