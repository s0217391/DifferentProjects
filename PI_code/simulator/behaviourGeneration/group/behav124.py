#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] + prey[0]
	temp1 = max( temp0 , otherHunter[0] )
	temp1 = dist * otherHunter[1]
	temp0 = prey[0] * temp1
	return [ prey[0] , dist ]
