#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = -1 * prey[0]
	temp1 = max(temp0, temp1)
	temp0 = max(temp0, prey[0])
	temp2 = temp0 + prey[0]
	temp2 = prey[0] + temp0
	if temp0 != 0:
		temp0 = temp1 % temp0
	else:
		temp0 = temp0
	if temp1 != 0:
		temp3 = prey[0] % temp1
	else:
		temp3 = temp1
	if prey[1] != 0:
		temp2 = temp0 / prey[1]
	else:
		temp2 = prey[1]
	temp1 = -1 * temp0
	temp0 = -1 * prey[0]
	temp4 = temp1 + temp1
	temp0 = max(temp0, temp0)
	temp3 = min(prey[0], temp2)
	if prey[0] != 0:
		temp5 = temp4 % prey[0]
	else:
		temp5 = prey[0]
	temp6 = min(temp4, temp0)
	temp2 = max(temp5, prey[1])
	temp2 = max(temp5, temp5)
	temp0 = temp6 + prey[1]
	return [temp1, prey[0]]
