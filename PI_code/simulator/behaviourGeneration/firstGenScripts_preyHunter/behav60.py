#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	if temp0 > temp0:
		temp1 = min(prey[1], temp0)
	else:
		temp1 = min(temp0, temp0)
	if prey[1] != 0:
		temp0 = temp0 / prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * prey[0]
	if prey[0] > prey[0]:
		temp1 = min(prey[1], prey[0])
	else:
		temp1 = max(prey[1], temp0)
	temp2 = temp0 + temp0
	if prey[0] > temp0:
		temp2 = temp1 * temp0
	else:
		temp2 = max(temp1, prey[0])
	temp3 = min(prey[0], temp2)
	return [temp1, temp0]
