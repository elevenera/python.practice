print "How old are you?",
age = int(raw_input())
print "How tall are you?",
height = int(raw_input())
print "How much do you weight?",
weight = int(raw_input())

print "So, you're %r old, %r tall and %r heavy." % (
      age, height, weight)
print "If I add %r, %r and %r I get %r." % (
      age, height, weight, age+height+weight)