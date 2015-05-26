#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	temp1 = max(prey[1], prey[0])
	temp2 = prey[0] + temp0
	if temp2 != 0:
		temp2 = prey[1] % temp2
	else:
		temp2 = temp2
	temp2 = temp0 - temp1
	if prey[1] != 0:
		temp3 = temp0 / prey[1]
	else:
		temp3 = prey[1]
	if prey[0] != 0:
		temp0 = temp1 / prey[0]
	else:
		temp0 = prey[0]
	temp4 = temp3 * temp0
	if temp0 != 0:
		temp2 = temp0 / temp0
	else:
		temp2 = temp0
	if temp2 != 0:
		temp3 = prey[1] / temp2
	else:
		temp3 = temp2
	temp0 = temp0 - temp0
	temp0 = max(temp0, temp1)
	temp2 = temp0 + prey[0]
	temp4 = max(temp2, temp3)
	if temp1 != 0:
		temp3 = prey[0] / temp1
	else:
		temp3 = temp1
	temp3 = min(temp3, temp0)
	return [temp4, temp4]
