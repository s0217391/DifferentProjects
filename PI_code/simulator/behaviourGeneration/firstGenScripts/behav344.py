#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = min(prey[0], temp0)
	temp0 = temp1 + temp0
	if temp0 != 0:
		temp2 = prey[1] / temp0
	else:
		temp2 = temp0
	temp0 = max(prey[1], temp2)
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	if temp2 != 0:
		temp0 = temp1 % temp2
	else:
		temp0 = temp2
	return [temp1, prey[1]]
