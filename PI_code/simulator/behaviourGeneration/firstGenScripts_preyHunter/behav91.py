#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[1]
	temp1 = max(temp0, prey[0])
	if temp0 != 0:
		temp0 = temp1 % temp0
	else:
		temp0 = temp0
	if temp1 > temp0:
		temp1 = prey[0] + temp1
	else:
		temp1 = min(prey[0], temp1)
	if temp1 > temp1:
		temp2 = max(prey[1], prey[0])
	else:
		temp2 = min(prey[1], temp0)
	temp1 = -1 * prey[0]
	if temp2 != 0:
		temp1 = temp2 % temp2
	else:
		temp1 = temp2
	return [prey[0], temp0]
