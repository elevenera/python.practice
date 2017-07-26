name = 'eleven'
age = 30 # not a lie
height = 74 # inches
height1 =round(74 *2.54 )# cm
weight = 180 # ibs
weight1 = 180 * 0.45 # kg
eyes ='Blue'
teech ='white'
hair ='brown'

print "Let's talk about %r." % name
print "He's %r cm tall." % height1
print "He's %r kg heavy." % weight1
print "Actually that's not too heavy."
print "He's got %s eyes and %r hair." % (eyes, hair)
print "His teech are usually %r depending on the coffee." % teech

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age,height, weight, age +height + weight)

