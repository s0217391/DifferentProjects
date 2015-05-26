#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	temp2 = -1 * temp1
	temp0 = prey[1] - prey[1]
	temp1 = temp0 * temp2
	temp2 = temp0 + temp0
	temp3 = max(temp2, temp0)
	if temp3 > temp2:
		temp4 = max(temp3, temp2)
	else:
		temp4 = min(temp2, temp2)
	temp1 = temp2 + temp1
	if temp1 != 0:
		temp5 = temp3 % temp1
	else:
		temp5 = temp1
	temp3 = -1 * temp5
	if temp2 != 0:
		temp6 = temp4 % temp2
	else:
		temp6 = temp2
	return [prey[1], temp4]
