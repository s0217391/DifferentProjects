#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[0])
	temp1 = temp0 - prey[1]
	if temp1 != 0:
		temp2 = prey[0] % temp1
	else:
		temp2 = temp1
	if temp1 > prey[1]:
		temp0 = temp2 - temp0
	else:
		temp0 = min(temp1, temp0)
	if temp1 != 0:
		temp3 = temp0 % temp1
	else:
		temp3 = temp1
	if prey[1] != 0:
		temp0 = temp1 % prey[1]
	else:
		temp0 = prey[1]
	temp2 = temp3 + prey[1]
	return [temp2, prey[0]]
