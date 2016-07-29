#!/usr/bin/python

import sys

meal = float(sys.argv[1])
tip = float(sys.argv[2])
tax = float(sys.argv[3])
 
tax_value = meal * tax
meal_with_tax = tax_value + meal
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value
 
print "The base cost of your meal was ${0:.2f}.".format(meal)
print "You need to pay ${0:.2f} for tax.".format(tax_value)
print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
                                                        int(100*tax), tax_value)
#note how we split up the line above across two lines. this is because
#the best practice in Python is to not exceed 80 characterse per line.
#This makes it much easier for you and others to read your code -- you don't have
#to scroll to read!
 
print "The grand total of your meal is ${0:.2f}.".format(total)
