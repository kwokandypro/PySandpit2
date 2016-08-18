#!/usr/bin/python
import sys

meal = float(sys.argv[1])
tax=0.02
tip=float(sys.argv[2])
tax_value=tax*meal
meal_with_tax=meal+tax_value
tip_value=meal*tip
total=(meal_with_tax+tip_value)

print "the base cost of the meal is %s, the tax is %s " % (meal,tax)
print "the tax is" + str(tax_value)
print "the tip will be" + str(tip)
print "the total of the meal is" + str(total)



