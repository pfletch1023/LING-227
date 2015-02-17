# LING 227 Homework 2
# Paul Fletcher-Hill (prf8)
# February 15, 2015

# import sys to make command line arguments accessible
import sys

def init_table(n, m):
  # Init table list
  return [[0 for j in range(m + 1)] for i in range(n + 1)]

# Arg is letter to insert
def ins_cost(letter):
  return 1

# Arg is letter to delete
def del_cost(letter):
  return 1

# Args are letter to delete, then letter to insert
def sub_cost(letter_old, letter_new):
  return 0 if letter_new is letter_old else 2

def min_edit(source, target):
  # Init length vars
  n = len(source)
  m = len(target)

  # Init table
  table = init_table(n, m)

  # Init D(i, 0) for all i = 1..n
  for i in range(1, n + 1):
    table[i][0] = table[i - 1][0] + del_cost(source[i - 1])

  # Init D(0, j) for all j = 1..m
  for j in range(1, m + 1):
    table[0][j] = table[0][j - 1] + ins_cost(target[j - 1])

  # Loop
  for i in range(1, n + 1):
    for j in range(1, m + 1):

      # Init source, target letter vars
      source_letter = source[i - 1]
      target_letter = target[j - 1]

      # Compute min and insert into table
      table[i][j] = min(
        table[i - 1][j] + del_cost(source_letter), 
        table[i][j - 1] + ins_cost(target_letter), 
        table[i - 1][j - 1] + sub_cost(source_letter, target_letter)
      )

  # Return D(n, m)
  return table[n][m]

# Store command line args as source and target
try:
  source = sys.argv[1]
  target = sys.argv[2]
except IndexError:
  print "Please provide at least two arguments"
  exit()

distance = min_edit(source, target)
print "Minimum edit distance from {0} to {1}: {2}".format(source, target, distance)
