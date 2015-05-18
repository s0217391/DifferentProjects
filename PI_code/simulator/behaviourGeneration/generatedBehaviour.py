#!/usr/bin/python
import sys
import numpy as np

def compute(prey):
	temp0 = prey[0] + prey[1]
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	temp0 = max(temp1, temp1)
	temp0 = temp1 + temp0
	temp2 = prey[0] + temp0
	temp2 = min(temp1, temp2)
	temp2 = min(temp0, temp2)
	temp0 = -1 * prey[0]
	temp2 = temp2 * prey[1]
	temp2 = prey[0] + prey[0]
	temp3 = temp0 + prey[1]
	if temp1 != 0:
		temp2 = temp3 % temp1
	else:
		temp2 = temp1
	temp2 = max(temp0, temp0)
	if temp0 != 0:
		temp0 = temp1 % temp0
	else:
		temp0 = temp0
	if prey[1] != 0:
		temp2 = prey[1] / prey[1]
	else:
		temp2 = prey[1]
	temp3 = min(prey[1], temp2)
	return np.array([prey[1], temp3])
