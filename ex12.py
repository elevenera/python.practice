age = int (raw_input("How old are you?"))
height = int(raw_input("How tall are you?"))
weight = int(raw_input("How much do you weight?"))

print "So, you're %r old, %r tall and %r heavy." % (
      age, height, weight)
print "If I add %r, %r and %r I get %r." % (
      age, height, weight, age+height+weight)