#!/usr/bin/python

import sys

meal = float(sys.argv[1])
tip=float(sys.argv[2])
tax=0.02
tax_value=tax*meal
meal_with_tax=meal+tax_value
tip_value=meal*tip
total=(meal_with_tax+tip_value)

print "the base cost of the meal is {:.2f}".format(meal)
print "the tax is %.2f" % tax
print "the tip will be " + str(tip)
print "the total of the meal is " + str(total)



