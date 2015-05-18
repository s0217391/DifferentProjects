#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[1]
	if temp0 != 0:
		temp1 = prey[0] / temp0
	else:
		temp1 = temp0
	if temp0 > prey[0]:
		temp2 = temp1 * temp0
	else:
		temp2 = min(temp1, temp1)
	temp1 = min(prey[0], prey[1])
	temp2 = temp0 + temp0
	temp1 = min(temp0, temp2)
	temp2 = prey[0] + prey[0]
	temp0 = max(prey[0], temp2)
	temp1 = max(temp1, temp0)
	if temp2 != 0:
		temp0 = temp0 / temp2
	else:
		temp0 = temp2
	if prey[1] != 0:
		temp3 = temp2 / prey[1]
	else:
		temp3 = prey[1]
	if temp3 != 0:
		temp1 = prey[1] % temp3
	else:
		temp1 = temp3
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	temp4 = -1 * temp2
	if prey[0] != 0:
		temp4 = prey[0] % prey[0]
	else:
		temp4 = prey[0]
	temp5 = temp4 * temp0
	temp0 = temp3 * temp5
	return [temp5, temp4]
