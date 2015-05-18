#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	if prey[1] != 0:
		temp1 = prey[1] % prey[1]
	else:
		temp1 = prey[1]
	temp2 = prey[1] * temp0
	if temp1 != 0:
		temp0 = temp2 / temp1
	else:
		temp0 = temp1
	if temp0 != 0:
		temp2 = prey[1] / temp0
	else:
		temp2 = temp0
	temp0 = min(temp2, prey[1])
	temp3 = max(temp2, prey[1])
	return [temp3, temp1]
