#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[0]
	if prey[1] > prey[1]:
		temp1 = max(temp0, prey[0])
	else:
		temp1 = prey[1] - temp0
	temp2 = temp0 + prey[0]
	if prey[0] != 0:
		temp3 = temp2 % prey[0]
	else:
		temp3 = prey[0]
	temp3 = temp3 + prey[0]
	temp4 = min(prey[1], temp2)
	temp1 = temp4 + temp1
	temp3 = prey[1] - temp4
	if temp2 > prey[0]:
		if temp3 != 0:
			temp4 = temp1 % temp3
		else:
			temp4 = temp3
	else:
		temp4 = prey[0] - temp3
	temp5 = temp2 - temp1
	temp2 = min(prey[1], temp3)
	temp0 = prey[0] + temp1
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp5 = min(temp1, temp2)
	temp6 = min(temp2, temp4)
	temp2 = temp6 + temp2
	if temp1 != 0:
		temp0 = temp5 % temp1
	else:
		temp0 = temp1
	if prey[1] > prey[0]:
		if temp2 != 0:
			temp5 = prey[0] % temp2
		else:
			temp5 = temp2
	else:
		temp5 = prey[1] + prey[1]
	if temp2 != 0:
		temp7 = temp4 / temp2
	else:
		temp7 = temp2
	return [temp7, temp0]
