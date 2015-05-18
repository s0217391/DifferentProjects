#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	temp1 = temp0 + prey[1]
	temp0 = -1 * temp0
	if temp0 > prey[1]:
		temp2 = temp0 + prey[0]
	else:
		temp2 = min(temp0, temp1)
	if temp0 != 0:
		temp3 = temp1 / temp0
	else:
		temp3 = temp0
	temp0 = -1 * temp2
	temp3 = temp2 + temp0
	if temp3 != 0:
		temp2 = temp3 / temp3
	else:
		temp2 = temp3
	temp3 = temp2 + temp2
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	if temp1 != 0:
		temp2 = prey[0] % temp1
	else:
		temp2 = temp1
	temp2 = temp2 + temp1
	temp1 = min(temp2, prey[0])
	if temp0 > temp1:
		temp1 = min(temp2, prey[0])
	else:
		temp1 = prey[1] * prey[0]
	temp4 = temp0 * temp1
	temp5 = -1 * temp2
	temp6 = temp0 * prey[0]
	temp2 = -1 * prey[0]
	temp5 = max(temp2, temp5)
	temp7 = -1 * temp5
	return [prey[0], temp2]
