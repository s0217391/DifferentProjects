#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	if prey[0] != 0:
		temp1 = temp0 % prey[0]
	else:
		temp1 = prey[0]
	temp2 = prey[1] - prey[0]
	if prey[1] != 0:
		temp1 = temp1 / prey[1]
	else:
		temp1 = prey[1]
	if prey[1] != 0:
		temp2 = temp2 / prey[1]
	else:
		temp2 = prey[1]
	temp0 = temp1 + temp2
	temp2 = temp2 - prey[1]
	temp1 = min(temp1, prey[0])
	if temp1 > temp2:
		temp1 = temp2 - temp0
	else:
		temp1 = temp2 - temp0
	temp3 = temp0 - prey[0]
	temp4 = temp3 + temp1
	if prey[1] != 0:
		temp0 = temp1 / prey[1]
	else:
		temp0 = prey[1]
	temp4 = temp3 - temp0
	if temp3 > temp0:
		temp3 = temp0 - temp2
	else:
		temp3 = prey[0] * prey[1]
	return [temp3, prey[1]]
