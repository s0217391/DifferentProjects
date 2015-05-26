#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[0])
	temp1 = max(prey[0], prey[0])
	temp0 = max(temp0, temp0)
	if temp1 != 0:
		temp2 = prey[0] % temp1
	else:
		temp2 = temp1
	temp3 = prey[1] + prey[0]
	temp4 = prey[0] * temp2
	if temp3 != 0:
		temp1 = temp4 % temp3
	else:
		temp1 = temp3
	temp3 = min(temp0, prey[1])
	temp4 = prey[1] + temp4
	temp1 = min(temp1, temp0)
	temp0 = max(temp4, temp1)
	if temp3 != 0:
		temp5 = temp0 / temp3
	else:
		temp5 = temp3
	temp6 = temp0 + prey[0]
	temp5 = temp5 + prey[0]
	return [temp6, prey[0]]
