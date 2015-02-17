# LING 227 Homework 2
# Paul Fletcher-Hill (prf8)
# February 15, 2015

# import sys to make command line arguments accessible
import sys
import operator

# QWERTY adjacent keys
adj_keys = {
  'q': ['a', 'w'],
  'w': ['q', 'a', 's', 'e'],
  'e': ['w', 's', 'd', 'r'],
  'r': ['e', 'd', 'f', 't'],
  't': ['r', 'f', 'g', 'y'],
  'y': ['t', 'g', 'h', 'u'],
  'u': ['y', 'h', 'j', 'i'],
  'i': ['u', 'j', 'k', 'o'],
  'o': ['i', 'k', 'l', 'p'],
  'p': ['o', 'l'],
  'a': ['q', 'w', 's', 'z'],
  's': ['w', 'e', 'a', 'd', 'z', 'x'],
  'd': ['e', 'r', 's', 'f', 'x', 'c'],
  'f': ['r', 't', 'd', 'g', 'c', 'v'],
  'g': ['t', 'y', 'f', 'h', 'v', 'b'],
  'h': ['y', 'u', 'g', 'j', 'b', 'n'],
  'j': ['u', 'i', 'h', 'k', 'n', 'm'],
  'k': ['i', 'o', 'j', 'l', 'm'],
  'l': ['o', 'p', 'k'],
  'z': ['a', 's', 'x'],
  'x': ['s', 'd', 'z', 'c'],
  'c': ['d', 'f', 'x', 'v'],
  'v': ['f', 'g', 'c', 'b'],
  'b': ['g', 'h', 'v', 'n'],
  'n': ['h', 'j', 'b', 'n'],
  'm': ['j', 'k', 'n']
}

# Vowels
vowels = ['a', 'e', 'i', 'o', 'u']

def adj(letter_old, letter_new):
  return letter_old in adj_keys.keys() and letter_new in adj_keys[letter_old]


def letter_i(string, index):
  try:
    return string[index]
  except IndexError:
    return None

def init_table(n, m):
  # Init table list
  return [[0 for j in range(m + 1)] for i in range(n + 1)]

# Arg is letter to insert
def ins_cost(letter):
  return 0.75

# Arg is letter to delete
def del_cost(letter):
  return 1

# Args are letter to delete, then letter to insert
def sub_cost(letter_old, letter_new):
  old_vowel = letter_old in vowels
  new_vowel = letter_new in vowels
  if old_vowel and new_vowel:
    cost = 1
  elif (old_vowel and not new_vowel) or (new_vowel and not old_vowel):
    cost = 1.75
  else:
    cost = 1.5
  return 0 if letter_new is letter_old else cost

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
      source_letter = letter_i(source, i - 1)
      last_source_letter = letter_i(source, i - 2)
      target_letter = letter_i(target, j - 1)
      last_target_letter = letter_i(target, j - 2)

      # Compute min and insert into table
      table[i][j] = min(
        table[i - 1][j] + del_cost(source_letter),
        table[i][j - 1] + ins_cost(target_letter), 
        table[i - 1][j - 1] + sub_cost(source_letter, target_letter)
      )

      # Damerau-Levenshtein distance (transposition)
      trans_bool = source_letter is last_target_letter and last_source_letter is target_letter
      if i > 1 and j > 1 and trans_bool:
        table[i][j] = min(
          table[i][j],
          table[i - 2][j - 2] + sub_cost(source_letter, target_letter)
        )

  # Return D(n, m)
  return table[n][m]

# Store command line args as filenames
try:
  dict_filename = sys.argv[1]
  filename = sys.argv[2]
except IndexError:
  print "Please provide at least two arguments"
  exit()

# Open dictionary and file for reading
dict_file = open(dict_filename, 'r')
dict = dict_file.read().splitlines()
file = open(filename, 'r')

# For each line in lines (mispellings)
for line in file:
  closest = None
  min_distance = 0
  for word in dict:
    distance = min_edit(line, word)
    if (closest is None) or (closest is not None and distance <= min_distance):
      closest = word
      min_distance = distance
  print closest

