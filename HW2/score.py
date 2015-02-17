import sys

of = open(sys.argv[1], 'r') # this is the output of the spellchecker
cf = open(sys.argv[2], 'r') # this is the target correction file
mf = open(sys.argv[3], 'r') # Mispellings file

correct = 0.0
incorrect = []

#reading both files as lists of lines
lineso = of.readlines()
linesc = cf.readlines()
linesm = mf.readlines()

#if the files are different lengths we exit
if len(lineso) != len(linesc):
    print "Your files are not the same length...exiting"
    exit(1)

for lineo in lineso: #go through each of our outputs
    linec = linesc.pop(0).strip() #grabbing next line from corrections file and stripping new lines off
    # the corrections file may have multiple words so we split
    linem = linesm.pop(0).strip()
    cwords = linec.split(', ')
    if lineo.strip() in cwords:
      correct += 1
    else:
      incorrect.append([linem, lineo.strip(), cwords])
    
print "Accuracy is", correct/len(lineso)
print "Incorrects:"
for inc in incorrect:
  print "{0:15} as {1:15} instead of {2:15}".format(inc[0], inc[1], ", ".join(inc[2]))
  #print inc[0], "as", inc[1], "instead of", ", ".join(inc[2])
