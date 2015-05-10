#!/usr/bin/python
import sys
import numpy as np

def compute(prey):
	print "DROLDROLDROLDROLDROLDROL"
	temp0 = prey[0] * prey[1]
	if temp0 != 0: temp1 = temp0 / temp0
	else: temp1 = temp0
	if temp1 != 0: temp0 = temp0 % temp1
	else: temp0 = temp0
	if temp0 != 0: temp2 = prey[0] / temp0
	else: temp2 = prey[0]
	temp3 = prey[0] + temp1
	if temp1 != 0: temp1 = temp0 % temp1
	else: temp1 = temp0
	if temp1 != 0: temp4 = temp0 / temp1
	else: temp4 = temp0
	temp3 = temp4 * prey[0]
	temp3 = prey[1] + temp4
	temp5 = prey[1] + prey[0]
	if temp2 != 0: temp3 = temp0 / temp2
	else: temp3 = temp0
	temp3 = min(temp3, temp5)
	if temp1 != 0: temp0 = temp1 / temp1
	else: temp0 = temp1
	temp3 = max(temp0, temp2)
	temp4 = temp0 * prey[1]
	temp1 = prey[1] - temp4
	return np.array([temp5, temp2])
