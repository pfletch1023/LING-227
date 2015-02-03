# LING 227 Assignment 1
# Factorial Exercise
# Paul Fletcher-Hill (prf8)
# January 20, 2015

# import sys to make command line arguments accessible
import sys

# Store first command line arg as num
try:
  num = int(sys.argv[1])
except ValueError:
  print "Please provide a positive integer"
  exit()
except IndexError:
  print "Please provide at least one argument"
  exit()

# Check that num is non-negative
if num < 0:
  print "Please provide a non-negative number"
  exit()

# Return for 0 case
if num == 0:
  print "The factorial of 0 is 0!"
  exit()

# Positive case
nums = range(1, num + 1)
fact = reduce(lambda x, y: x*y, nums)
print "The factorial of " + str(num) + " is " + str(fact) + "!"
