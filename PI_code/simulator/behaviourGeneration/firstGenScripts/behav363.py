#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[1])
	temp1 = -1 * prey[1]
	temp2 = temp0 * prey[1]
	temp0 = min(prey[0], temp0)
	temp3 = prey[0] - temp0
	temp4 = -1 * prey[0]
	temp0 = temp2 + temp3
	if temp0 != 0:
		temp0 = temp0 % temp0
	else:
		temp0 = temp0
	temp3 = prey[1] - prey[1]
	temp2 = -1 * prey[0]
	temp4 = min(temp2, temp4)
	temp1 = max(temp4, prey[0])
	if prey[0] != 0:
		temp5 = temp1 / prey[0]
	else:
		temp5 = prey[0]
	if temp5 != 0:
		temp4 = temp3 / temp5
	else:
		temp4 = temp5
	if prey[0] != 0:
		temp3 = prey[0] % prey[0]
	else:
		temp3 = prey[0]
	temp5 = temp4 + temp1
	temp1 = min(temp5, temp2)
	if temp4 != 0:
		temp5 = temp5 % temp4
	else:
		temp5 = temp4
	temp4 = temp1 + temp4
	temp4 = max(prey[1], temp4)
	return [temp2, temp4]
