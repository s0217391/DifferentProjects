#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[1] + prey[0]
	temp1 = min(temp0, temp1)
	temp1 = temp0 - temp0
	temp0 = temp1 + temp0
	if temp0 > prey[0]:
		temp2 = min(prey[0], prey[1])
	else:
		temp2 = -1 * prey[0]
	if temp1 > temp1:
		temp1 = prey[0] - temp1
	else:
		temp1 = prey[1] + prey[0]
	temp2 = temp0 - prey[0]
	if prey[0] != 0:
		temp3 = temp0 / prey[0]
	else:
		temp3 = prey[0]
	if prey[0] != 0:
		temp3 = temp2 % prey[0]
	else:
		temp3 = prey[0]
	temp3 = -1 * temp3
	temp2 = -1 * prey[0]
	temp2 = max(temp0, temp0)
	temp2 = max(temp3, temp3)
	temp4 = temp1 * temp1
	temp2 = max(temp3, temp4)
	return [temp0, temp2]
