# this is a command line version of fib

# import sys to make command line arguments accessible
import sys

# The following is a multiline comment

'''
store first argument as 'num', 
first check that user provided a number
if not, exit gracefully
'''
try:
    num = int(sys.argv[1])
except ValueError:
    print "Please provide a positive integer"
    exit()

# set first two numbers to 0, 1
fib1,fib2  = 0,1

# check to make sure num is a valid position, otherwise exit
if num < 1:
    print "Please give me a postive integer and try again"
    exit()

# print first one or two numbers of the sequence, depending on num
print "The fib number at 1 is " + str(fib1)
if num>=2: print "The fib number at 2 is", fib2

# print out the fibonacci sequence from 3 to num 
i=3
while i <= num:
    fib1, fib2 = fib2, fib1 + fib2
    print "The fib number at position " + str(i) + " is " + str(fib2)
    i += 1
 