from __future__ import division

def add(x,y):
	# Function to Add numbers
	return x+y

def subtract(x,y):
	# Function to Subtract numbers
	return x-y

def multiply(x,y):
	# Function to Multiply numbers
	return x*y

def divide(x,y):
	# Function to Divide numbers
	if y==0:
		raise ValueError('Cannot Divide by Zero!!!')
	return x / y