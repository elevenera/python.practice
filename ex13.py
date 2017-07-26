from sys import argv

script, first, second, third, forth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "your forth variable is:", forth

old = raw_input('old ???')
height = raw_input('height?')
weight = raw_input('weight?')

print " I was %r years old, %s tall and %s heavy." % (old, height, weight)