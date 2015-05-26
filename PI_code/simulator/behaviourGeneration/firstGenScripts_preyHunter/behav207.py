#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[1]
	temp1 = prey[0] - prey[1]
	temp2 = prey[1] * temp0
	return [temp0, temp2]
