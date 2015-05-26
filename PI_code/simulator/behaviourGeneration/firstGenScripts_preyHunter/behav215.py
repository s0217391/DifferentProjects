#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[0])
	temp1 = temp0 + temp0
	temp0 = max(temp1, temp1)
	if prey[0] != 0:
		temp2 = temp0 / prey[0]
	else:
		temp2 = prey[0]
	if temp2 != 0:
		temp1 = temp0 / temp2
	else:
		temp1 = temp2
	temp3 = max(prey[0], prey[1])
	temp2 = max(prey[0], temp1)
	temp3 = min(temp1, prey[0])
	temp1 = -1 * temp3
	if prey[1] > prey[0]:
		temp2 = min(temp1, temp2)
	else:
		temp2 = temp2 + prey[0]
	temp1 = -1 * temp0
	if temp2 > temp0:
		temp3 = prey[0] * temp1
	else:
		temp3 = temp2 - temp3
	temp0 = temp3 + prey[0]
	temp3 = max(temp1, temp0)
	return [temp1, prey[0]]
