#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[0] * prey[1]
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	if temp2 != 0:
		temp1 = temp0 % temp2
	else:
		temp1 = temp2
	temp2 = max(temp2, temp0)
	temp3 = max(temp0, temp0)
	if prey[1] != 0:
		temp1 = temp2 % prey[1]
	else:
		temp1 = prey[1]
	if temp0 != 0:
		temp4 = temp3 % temp0
	else:
		temp4 = temp0
	temp1 = max(temp4, prey[1])
	temp0 = -1 * temp1
	if temp0 != 0:
		temp5 = temp1 % temp0
	else:
		temp5 = temp0
	temp5 = max(temp5, temp4)
	return [temp1, temp1]
