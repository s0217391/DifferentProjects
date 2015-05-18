#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[1]
	temp1 = prey[1] + prey[0]
	temp0 = max(prey[0], temp0)
	if temp1 != 0:
		temp2 = temp0 % temp1
	else:
		temp2 = temp1
	if prey[1] > temp2:
		temp1 = -1 * temp1
	else:
		temp1 = temp2 - temp1
	temp3 = -1 * temp0
	temp2 = prey[0] + prey[1]
	temp3 = temp1 + temp1
	if temp2 != 0:
		temp1 = prey[1] % temp2
	else:
		temp1 = temp2
	if temp3 > temp2:
		temp1 = prey[1] - prey[0]
	else:
		temp1 = -1 * temp1
	if temp0 != 0:
		temp2 = temp3 / temp0
	else:
		temp2 = temp0
	temp1 = temp2 + temp3
	temp0 = prey[0] + prey[0]
	temp3 = max(temp2, temp2)
	return [temp1, temp1]