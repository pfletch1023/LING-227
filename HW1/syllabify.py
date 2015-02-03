# LING 227 Homework 1
# Paul Fletcher-Hill (prf8)
# February 1, 2015

# import sys to make command line arguments accessible
import sys

# Syllable constituents
ONSET = 0
NUCLEI = 1
CODA = 2

# this dictionary encodes the sonority level of each phoneme
son = {
  'AA': 4, 'AE' : 4, 'AH' : 4, 'AO' : 4, 'AW' : 4, 'AY' : 4,
  'B'  : 0, 'CH' : 0, 'D' : 0, 'DH' : 0, 'EH' : 4, 'ER' : 4,
  'EY' : 4, 'F': 0, 'G': 0, 'HH': 0, 'IH': 4, 'IY': 4, 'JH': 0,
  'K': 0, 'L': 2, 'M': 1, 'N': 1, 'NG': 1, 'OW': 4, 'OY': 4,
  'P': 0, 'R': 2, 'S': 0, 'SH': 0, 'T': 0, 'TH': 0, 'UH': 4,
  'UW': 4, 'V': 0, 'W': 3, 'Y': 3, 'Z': 0, 'ZH': 0
}

# Build string from list of phons and dictionary of phon classifications
def string_from_syllables(phons, syllables):
  string = ""
  for i, phon in enumerate(phons):
    if i > 0:
      if syllables[i - 1] > syllables[i]:
        string += (" + " + phon)
      elif syllables[i - 1] == NUCLEI and syllables[i] == NUCLEI:
        string += (" + " + phon)
      else:
        string += (" " + phon)
    else:
      string += phon
  return string

def syllabify(phons):

  # Init syllables list (default to CODA)
  syllables = [CODA] * len(phons)

  # Define first_nuclei
  first_nuclei = 0
  while son[phons[first_nuclei]] != 4:
    first_nuclei += 1

  # Reverse first_nuclei
  first_nuclei = len(phons) - 1 - first_nuclei

  # Init last_nuclei
  last_nuclei = None

  # Reverse phons list for traversal
  reversed_phons = phons[::-1]

  # For each phon in reversed phons list
  for i, phon in enumerate(reversed_phons):

    # Vowel and set last_nuclei if None
    if son[phon] == 4:
      syllables[i] = NUCLEI
      if not last_nuclei:
        last_nuclei = i

    # If last_nuclei has already passed
    elif last_nuclei is not None:

      # Init Onset Maximization values
      last = reversed_phons[i - 1]
      son_diff = son[last] - son[phon]

      # Before first NUCLEI => ONSET
      if i > first_nuclei:
        syllables[i] = ONSET

      # Directly before NUCLEI => ONSET
      elif syllables[i - 1] == NUCLEI:
        syllables[i] = ONSET

      # Onset Maximization => ONSET
      elif syllables[i - 1] == ONSET and son_diff >= 2:
        syllables[i] = ONSET

      # S => ONSET
      elif phon == "S":
        syllables[i] = CODA

  return string_from_syllables(phons, syllables[::-1])

def update_syllables_dict(dict, line):
  for syllable in line.split(" + "):
    pattern = ""
    for phon in syllable.split():
      if son[phon] > 3:
        pattern += "C"
      else:
        pattern += "V"
    if pattern in dict:
      dict[pattern] += 1
    else:
      dict[pattern] = 1
  return dict

# Store first command line arg as filename
try:
  filename = sys.argv[1]
except IndexError:
  print "Please provide at least one file name"
  exit()

# Open file for reading
file = open(filename, 'r')

# Syllables dictionary
syllables_dict = {}

# For each line in lines
for line in file:
  phons = line.split()[1:] # Return all but first el in list
  syllabified_line = syllabify(phons)
  print line.split()[0] + " " + syllabified_line
  syllables_dict = update_syllables_dict(syllables_dict, syllabified_line)

# print "\n"
# print "Syllable type frequencies:"
# total = sum(syllables_dict.values())
# for pattern, num in syllables_dict.items():
#   print "{0:20} {1:>10.2f}".format("Frequency of " + pattern + " :", (num * 100.0 / total))
