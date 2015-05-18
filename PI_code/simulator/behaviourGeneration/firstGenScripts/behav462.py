#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	if prey[1] > temp0:
		temp1 = temp1 - prey[1]
	else:
		temp1 = temp0 - temp0
	temp2 = min(temp1, prey[0])
	temp0 = temp0 + temp1
	temp1 = temp2 * temp2
	temp3 = min(temp0, temp2)
	temp1 = temp2 - temp0
	temp1 = -1 * temp3
	if temp3 != 0:
		temp1 = prey[1] / temp3
	else:
		temp1 = temp3
	temp0 = max(prey[0], temp0)
	temp3 = temp0 * temp1
	temp2 = prey[0] * temp1
	if prey[0] != 0:
		temp1 = temp1 / prey[0]
	else:
		temp1 = prey[0]
	if prey[1] != 0:
		temp0 = temp2 / prey[1]
	else:
		temp0 = prey[1]
	temp2 = -1 * prey[0]
	if temp1 != 0:
		temp0 = temp1 % temp1
	else:
		temp0 = temp1
	temp3 = temp1 * temp0
	temp2 = prey[1] + prey[1]
	return [temp0, prey[1]]
