#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] - prey[0]
	temp1 = prey[1] + prey[1]
	temp1 = otherHunter[0] - otherHunter[0]
	temp0 = min( otherHunter[1] , prey[0] )
	return [ prey[0] , temp1 ]
