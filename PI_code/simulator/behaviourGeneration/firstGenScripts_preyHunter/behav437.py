#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		temp0 = min(prey[1], prey[0])
	else:
		temp0 = prey[1] + prey[0]
	temp1 = max(prey[0], temp0)
	temp2 = max(temp1, prey[0])
	temp1 = min(prey[0], temp0)
	temp0 = max(temp2, temp2)
	temp1 = min(temp1, temp1)
	temp2 = max(temp2, temp0)
	temp0 = prey[1] - prey[1]
	temp3 = min(prey[0], temp1)
	if temp3 != 0:
		temp4 = temp0 % temp3
	else:
		temp4 = temp3
	if temp0 > temp1:
		temp4 = max(temp1, prey[1])
	else:
		temp4 = temp3 - temp4
	return [prey[1], temp3]
