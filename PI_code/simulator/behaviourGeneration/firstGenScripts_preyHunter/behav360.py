#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	temp1 = prey[0] + temp0
	if temp1 > temp0:
		if prey[1] != 0:
			temp2 = temp1 % prey[1]
		else:
			temp2 = prey[1]
	else:
		if temp0 != 0:
			temp2 = temp0 % temp0
		else:
			temp2 = temp0
	if temp2 != 0:
		temp3 = temp1 % temp2
	else:
		temp3 = temp2
	temp3 = temp0 + temp2
	return [temp1, prey[1]]
