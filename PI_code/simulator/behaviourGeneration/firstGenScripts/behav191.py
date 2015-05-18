#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[0] - temp0
	temp2 = prey[0] + temp0
	if temp1 != 0:
		temp3 = temp0 % temp1
	else:
		temp3 = temp1
	return [temp1, temp1]
