#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[1]
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	if prey[0] != 0:
		temp1 = temp1 % prey[0]
	else:
		temp1 = prey[0]
	if temp1 != 0:
		temp0 = prey[1] % temp1
	else:
		temp0 = temp1
	if prey[0] != 0:
		temp1 = prey[1] / prey[0]
	else:
		temp1 = prey[0]
	temp2 = max(prey[0], temp1)
	temp2 = min(temp2, prey[0])
	if temp0 != 0:
		temp1 = temp2 % temp0
	else:
		temp1 = temp0
	temp3 = temp2 + temp0
	temp0 = temp1 * prey[0]
	temp2 = -1 * temp2
	temp1 = temp1 - temp1
	temp1 = -1 * temp0
	temp1 = temp2 - temp2
	temp0 = -1 * temp1
	if temp2 != 0:
		temp3 = prey[1] % temp2
	else:
		temp3 = temp2
	if temp0 != 0:
		temp4 = temp0 % temp0
	else:
		temp4 = temp0
	temp5 = temp0 - temp0
	if temp3 != 0:
		temp3 = temp5 % temp3
	else:
		temp3 = temp3
	return [temp4, prey[0]]
